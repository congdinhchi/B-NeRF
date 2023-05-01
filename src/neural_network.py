import torch.nn as nn
import torch
from typing import Optional

# config
torch.manual_seed(0)
SKIP_ORDER = 4

class NeuralNetwork(nn.Module):
  r"""
  Mạng neural lõi
  """
  def __init__(self, d_coordinate: int = 3, d_viewdirs: int = 2,  n_layers: int = 8, d_filter: int = 256, skip: tuple[int] = (4,)) -> None:
    '''
    d_coordinate: dimension coordinate
    n_layers: số lớp
    d_filter: số feature của 1 lớp ẩn
    skip: vị trí skip connection thông tin input
    d_viewdirs: dimension 
    '''
    super().__init__()
    
    self.act = nn.functional.relu
    self.d_viewdirs = d_viewdirs
    list_layer = []

    # layer 0
    layer_0 = nn.Linear(d_coordinate, d_filter)
    list_layer.append(layer_0)

    # layer 0-7
    for i in range(n_layers - 1):
        if i == SKIP_ORDER:
            layer_tmp = nn.Linear(d_filter + d_coordinate, d_filter) 
        else:
            layer_tmp = nn.Linear(d_filter, d_filter)
        list_layer.append(layer_tmp)
    self.layers = nn.ModuleList(list_layer)

    # Đầu ra của các hidden layer
    self.hidden_filters = nn.Linear(d_filter, d_filter)
    self.alpha_out = nn.Linear(d_filter, 1)

    self.layer_input_3 = nn.Linear(d_viewdirs, d_filter)
    self.brightness_out = nn.Linear(d_filter, 1)

    self.branch = nn.Linear(d_filter + d_filter + self.d_viewdirs, d_filter // 2)
    self.rgb_out = nn.Linear(d_filter // 2, 3)
    
  def forward(self, x: torch.Tensor, viewdirs: Optional[torch.Tensor] = None) -> torch.Tensor:
    ''' 
    x: coordinate 
    '''

    # Đi qua các layer từ 1 đến 8
    for i, layer in enumerate(self.layers):
        x = self.act(layer(x))
        if i == SKIP_ORDER:
            x = torch.cat([x, coordinates], dim=-1)
    
    # output alpha
    alpha = self.alpha_out(x)

    # output brightness
    y = self.layer_input_3(viewdirs)
    y = self.act(y)
    y = self.hidden_filters(y)
    y = self.act(y)
    brightness = self.brightness_out(y)

    # output rgb
    x = self.hidden_filters(x)
    x = torch.concat([x, y, viewdirs], dim=-1)
    x = self.branch(x)
    x = self.act(x)
    rgb = self.rgb_out(x)

    return torch.concat([rgb, brightness, alpha], dim=-1)

     

# test
if __name__ == "__main__":
  model = NeuralNetwork()
  coordinates = torch.Tensor([-0.3032,  1.7914,  1.9560])
  viewdirs = torch.Tensor([-0.3032,  1.7914])
  result = model.forward(coordinates, viewdirs)
  print(result)

  # sample
  # tensor([ 0.0274,  0.0798, -0.0281, -0.0066], grad_fn=<AddBackward0>)