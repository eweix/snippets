---
library: pytorch
language: python
---

# pytorch

## PyTorch Imports

Common pytorch imports

<!-- pytorch-imports -->

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
```

## Check Device

Check the available device

<!-- pytorch-device -->

```python
device = torch.device('cuda:0' if torch.cuda.is_available() else 'mps' if torch.mps.is_available() else 'cpu')
```

## Optimizer

Select an optimizer

<!-- pytorch-optimizer -->

```python
optimizer = torch.optim.${1|Adadelta,Adagrad,Adam,SparseAdam,Adamax,ASGD,LBFGS,RMSprop,Rprop,SGD|}(${2:net}.parameters(), lr=${3:1e-2})
```

## Scheduler

Select a scheduler method to adjust the learning rate

<!-- pytorch-scheduler -->

```python
scheduler = torch.optim.lr_scheduler.${1|LambdaLR,StepLR,MultiStepLR,ExponentialLR,CosineAnnealingLR,ReduceLROnPlateau,CyclicLR|}(${2:optimizer})
```

## Dataset

Template for a custom dataset

<!-- pytorch-dataset -->

```python
class ${1:MyDataset}(torch.utils.data.Dataset):
	"""Some Information about ${1:MyDataset}"""
	def __init__(self):
		super(${1:MyDataset}, self).__init__()

	def __getitem__(self, index):
		return $2

	def __len__(self):
		return $3
```

## Dataloader

Template for a dataloader

<!-- pytorch-dataloader -->

```python
dataloader = torch.utils.data.DataLoader(${1:dataset}, batch_size=${2:1}, shuffle=${3|False,True|})
```

## Classification Loss

Select a loss function for classification provided by pytorch

<!-- pytorch-loss_class -->

```python
criterion = nn.${1|CrossEntropyLoss,NLLLoss,PoissonNLLLoss,BCELoss,BCEWithLogitsLoss,MarginRankingLoss,HingeEmbeddingLoss,MultiLabelMarginLoss,SoftMarginLoss,MultiLabelSoftMarginLoss,CosineEmbeddingLoss,MultiMarginLoss,TripletMarginLoss,CTCLoss|}()
```

## Regression Loss

Select a loss function for regression provided by pytorch

<!-- pytorch-loss_reg -->

```python
criterion = nn.${1|L1Loss,MSELoss,KLDivLoss,SmoothL1Loss|}()
```

## PyTorch Module

Creates a custom class template which inherits from torch.nn.Module

<!-- pytorch-module -->

```python
class ${1:MyModule}(nn.Module):
	"""Some Information about ${1:MyModule}"""
	def __init__(self):
		super(${1:MyModule}, self).__init__()

	def forward(self, x):

		return x
```

## Container

Stores modules or parameters in some kind of container

<!-- pytorch-container -->

```python
layers = nn.${1|Sequential,ModuleList,ModuleDict,ParameterList,ParameterDict|}($2)
```

## Fully Connected Block

Create a fully connected linear layer for a neural network.
Includes regularization and dropout normalization.

<!-- pytorch-fc|nn-fc -->

```python
nn.Linear(${in},${out},bias=False),
nn.ReLU(),
nn.Dropout(),
$0
```

## PyTorch Autograd Function

Creates a custom autograd function template which inherits from torch.autograd.Function

<!-- pytorch-function -->

```python
class ${1:MyFunction}(torch.autograd.Function):
	"""Some Information about ${1:MyFunction}"""

	@staticmethod
	def forward(ctx, input):

		return

	@staticmethod
	def backward(ctx, grad_output)

		return
```

## Initialize

Creates an initializer function and applies it to the given neural network

<!-- pytorch-init -->

```python
def init_weights(m):
	classname = m.__class__.__name__
	if classname.find('Linear') != -1 or classname.find('Bilinear') != -1:
		nn.init.${1|kaiming_uniform_(a=2\, mode='fan_in'\, nonlinearity='leaky_relu'\, ,kaiming_normal_(a=0\, mode='fan_in'\, nonlinearity='leaky_relu'\, ,xavier_uniform_(gain=1\, ,xavier_normal_(gain=1\, ,eye_(,orthogonal_(gain=1\, ,normal_(mean=0\, std=1\, ,uniform_(a=0\, b=1\, ,sparse_(sparsity=0.1\, std=0.01\, ,constant_(val=0.1\, ,zeros_(,ones_(|}tensor=m.weight)
		if m.bias: nn.init.${2|zeros(,uniform_(a=0\, b=1\, ,normal_(mean=0\, std=1\, ,ones_(,constant_(val=0.01\, |}tensor=m.bias)

	elif classname.find('Conv') != -1:
		nn.init.${3|kaiming_uniform_(a=2\, mode='fan_in'\, nonlinearity='leaky_relu'\, ,kaiming_normal_(a=0\, mode='fan_in'\, nonlinearity='leaky_relu'\, ,xavier_uniform_(gain=1\, ,xavier_normal_(gain=1\, ,dirac_(,orthogonal_(gain=1\, ,normal_(mean=0\, std=1\, ,uniform_(a=0\, b=1\, ,sparse_(sparsity=0.1\, std=0.01\, ,constant_(val=0.1\, ,zeros_(,ones_(|}tensor=m.weight)
		if m.bias: nn.init.${4|zeros(,normal_(mean=0\, std=1\, ,uniform_(a=0\, b=1\, ,ones_(,constant_(val=0.01\, |}tensor=m.bias)

	elif classname.find('BatchNorm') != -1 or classname.find('GroupNorm') != -1 or classname.find('LayerNorm') != -1:
		nn.init.${5|uniform_(a=0\, b=1\, ,normal_(mean=0\, std=1\, ,constant_(val=0.1\, ,zeros_(,ones_(|}tensor=m.weight)
		nn.init.${6|zeros(,normal_(mean=0\, std=1\, ,uniform_(a=0\, b=1\, ,ones_(,constant_(val=0.01\, |}tensor=m.bias)

	elif classname.find('Cell') != -1:
		nn.init.${7|xavier_uniform_(gain=1\, ,xavier_normal_(gain=1\, ,kaiming_uniform_(a=0\, mode='fan_in'\, nonlinearity='leaky_relu'\, ,kaiming_normal_(a=0\, mode='fan_in'\, nonlinearity='leaky_relu'\, ,eye_(,orthogonal_(gain=1\, ,normal_(mean=0\, std=1\, ,uniform_(a=0\, b=1\, ,sparse_(sparsity=0.1\, std=0.01\, ,constant_(val=0.1\, ,zeros_(,ones_(|}tensor=m.weight_hh)
		nn.init.${8|xavier_uniform_(gain=1\, ,xavier_normal_(gain=1\, ,kaiming_uniform_(a=0\, mode='fan_in'\, nonlinearity='leaky_relu'\, ,kaiming_normal_(a=0\, mode='fan_in'\, nonlinearity='leaky_relu'\, ,eye_(,orthogonal_(gain=1\, ,normal_(mean=0\, std=1\, ,uniform_(a=0\, b=1\, ,sparse_(sparsity=0.1\, std=0.01\, ,constant_(val=0.1\, ,zeros_(,ones_(|}tensor=m.weight_ih)
		nn.init.${9|ones_(,normal_(mean=0\, std=1\, ,uniform_(a=0\, b=1\, ,zeros(,constant_(val=0.01\, |}tensor=m.bias_hh)
		nn.init.${10|ones_(,normal_(mean=0\, std=1\, ,uniform_(a=0\, b=1\, ,zeros(,constant_(val=0.01\, |}tensor=m.bias_ih)

	elif classname.find('RNN') != -1 or classname.find('LSTM') != -1 or classname.find('GRU') != -1:
		for w in m.all_weights:
			nn.init.${11|xavier_uniform_(gain=1\, ,xavier_normal_(gain=1\, ,kaiming_uniform_(a=0\, mode='fan_in'\, nonlinearity='leaky_relu'\, ,kaiming_normal_(a=0\, mode='fan_in'\, nonlinearity='leaky_relu'\, ,eye_(,orthogonal_(gain=1\, ,normal_(mean=0\, std=1\, ,uniform_(a=0\, b=1\, ,sparse_(sparsity=0.1\, std=0.01\, ,constant_(val=0.1\, ,zeros_(,ones_(|}tensor=w[2].data)
			nn.init.${12|xavier_uniform_(gain=1\, ,xavier_normal_(gain=1\, ,kaiming_uniform_(a=0\, mode='fan_in'\, nonlinearity='leaky_relu'\, ,kaiming_normal_(a=0\, mode='fan_in'\, nonlinearity='leaky_relu'\, ,eye_(,orthogonal_(gain=1\, ,normal_(mean=0\, std=1\, ,uniform_(a=0\, b=1\, ,sparse_(sparsity=0.1\, std=0.01\, ,constant_(val=0.1\, ,zeros_(,ones_(|}tensor=w[3].data)
			nn.init.${13|ones_(,normal_(mean=0\, std=1\, ,uniform_(a=0\, b=1\, ,zeros(,constant_(val=0.01\, |}tensor=w[0].data)
			nn.init.${14|ones_(,normal_(mean=0\, std=1\, ,uniform_(a=0\, b=1\, ,zeros(,constant_(val=0.01\, |}tensor=w[1].data)

	if classname.find('Embedding') != -1:
		nn.init.${1|normal_(mean=0\, std=1\, ,xavier_uniform_(gain=1\, ,xavier_normal_(gain=1\, ,kaiming_uniform_(a=0\, mode='fan_in'\, nonlinearity='leaky_relu'\, ,kaiming_normal_(a=0\, mode='fan_in'\, nonlinearity='leaky_relu'\, ,eye_(,orthogonal_(gain=1\, ,uniform_(a=0\, b=1\, ,sparse_(sparsity=0.1\, std=0.01\, ,constant_(val=0.1\, ,zeros_(,ones_(|}tensor=m.weight)

${15:net}.apply(init_weights)
```

## Train Loop

Example for creating a simple training loop

<!-- pytorch-train -->

```python
# loop over the dataset multiple times
for epoch in range(${1:5}):
	running_loss = 0.0
	for i, data in enumerate(${2:trainloader}, 0):
		inputs, labels = data
		inputs, labels = inputs.to(${3:device}), labels.to(${3:device})

		# zero the parameter gradients
		${4:optimizer}.zero_grad()

		# forward + backward + optimize
		outputs = ${5:net}(inputs)
		loss = ${6:criterion}(outputs, labels)
		loss.backward()
		${4:optimizer}.step()

		running_loss += loss.item()

	print('Loss: {}'.format(running_loss))

print('Finished Training')
```

## Model Checkpoint



<!-- pytorch-checkpoint -->

```python
${1:model}.load_state_dict(${2|'path/to/model',torch.hub.load_state_dict_from_url('url')|})
```

## GitHub Checkpoint



<!-- pytorch-github -->

```python
${1:model} = torch.hub.load(github=${2:'pytorch/vision'}, model=${3:'resnet50'}, pretrained=${4|False,True|})
```

## Freeze Layers



<!-- pytorch-freeze -->

```python
for params in ${1:net}.parameters():
	params.require_grad = False
```

## Sampler



<!-- pytorch-sampler -->

```python
sampler = torch.utils.data.${1|Sampler(data_source),SequantialSample(data_source),RandomSampler(data_source),SubsetRandomSampler(indicies),WeightedRandomSampler(weights\, num_samples),BatchSampler(sampler\, batch_size\, drop_last),distributed.DistributedSampler(dataset)|}
```

## Unfreeze Layers



<!-- pytorch-unfreeze -->

```python
for params in ${1:net}.parameters():
	params.require_grad = True
```

## Activation

Adds a non-linear activation

<!-- pytorch-layer-activation -->

```python
${1:nonlin} = nn.${2|ELU(alpha=1.\, inplace=False),Hardshrink(lambd=0.5),Hardtanh(min_val=-1\, max_val=1\, inplace=False\, min_value=None\, max_value=None),LeakyReLU(negative_slope=0.01\, inplace=False),LogSigmoid,PReLU(num_parameters=1\, init=0.25),ReLU(inplace=False),ReLU6(inplace=False),RReLU(lower=0.125\, upper=0.3333333333333333\, inplace=False),CELU(alpha=1.0\, inplace=False),SELU(inplace=False),Sigmoid,Softplus(beta=1\, threshold=20),Softshrink(lambd=0.5),Softsign,Tanh,Tanhshrink,Threshold(threshold\, value\, inplace=False),Softmin(dim=None),Softmax(dim=None),Softmax2d,LogSoftmax(dim=None),AdaptiveLogSoftmaxWithLogits(in_features\, n_classes\, cutoffs\, div_value=4.0\, head_bias=True)|}
```

## Attention

Adds an attention layer

<!-- pytorch-layer-attention -->

```python
${1:mutli_attention} = nn.MultiheadAttention(embed_dim=$2, num_heads=$3)
```

## Convolution Layer

Creates a convolutional layer

<!-- pytorch-layer-conv -->

```python
${1:conv} = nn.${2|Conv1d(in_channel\, out_channel\, groups=1\, bias=True\, ,Conv2d(in_channel\, out_channel\, groups=1\, bias=True\, ,Conv3d(in_channel\, out_channel\, groups=1\, bias=True\, ,ConvTranspose1d(in_channel\, out_channel\, groups=1\, bias=True\, out_padding=0\, dilation=1\, ,ConvTranspose2d/in_channel\, out_channel\, groups=1\, bias=True\, out_padding=0\, dilation=1\, ,ConvTranspose3d(in_channel\, out_channel\, groups=1\, bias=True\, out_padding=0\, dilation=1\, ,Unfold(dilation=1\, ,Fold(output_size\, |}kernel_size=2, padding=0, stride=1)
```

## Pooling Layer

Creates a pooling layer

<!-- pytorch-layer-pooling -->

```python
${1:pool} = nn.${2|MaxPool1d(kernel_size\, stride=None\, padding=0\, dilation=1\, return_indices=False\, ceil_mode=False),MaxPool2d(kernel_size\, stride=None\, padding=0\, dilation=1\, return_indices=False\, ceil_mode=False),MaxPool3d(kernel_size\, stride=None\, padding=0\, dilation=1\, return_indices=False\, ceil_mode=False),MaxUnpool1d(kernel_size\, stride=None\, padding=0),MaxUnpool2d(kernel_size\, stride=None\, padding=0),MaxUnpool3d(kernel_size\, stride=None\, padding=0),AvgPool1d(kernel_size\, stride=None\, padding=0\, ceil_mode=False\, count_include_pad=True),AvgPool2d(kernel_size\, stride=None\, padding=0\, ceil_mode=False\, count_include_pad=True),AvgPool3d(kernel_size\, stride=None\, padding=0\, ceil_mode=False\, count_include_pad=True),FractionalMaxPool2d(kernel_size\, output_size=None\, output_ratio=None\, return_indices=False\, random_samples=None),LPPool1d(norm_type\, kernel_size\, stride=None\, ceil_mode=False),LPPool2d(norm_type\, kernel_size\, stride=None\, ceil_mode=False),AdaptiveMaxPool1d(output_size\, return_indices=False),AdaptiveMaxPool2d(output_size\, return_indices=False),AdaptiveMaxPool3d(output_size\, return_indices=False),AdaptiveAvgPool1d(output_size),AdaptiveAvgPool2d(output_size),AdaptiveAvgPool3d(output_size)|}
```

## Padding Layer

Creates a padding layer

<!-- pytorch-layer-padding -->

```python
${1:padding} = nn.${2|ReflectionPad1d(,ReflectionPad2d(,ReplicationPad1d(,ReplicationPad2d(,ReplicationPad3d(,ZeroPad2d(,ConstantPad1d(value=3.5\, ,ConstantPad2d(value=3.5\, ,ConstantPad3d(value=3.5\, |}padding=${3:(2,2)}
```

## Recurrent Layer

Creates a recurrent layer

<!-- pytorch:layer:recurrent -->

```python
${1:recurrent} = nn.${2|RNN,LSTM,GRU,RNNCell,LSTMCell,GRUCell|}(${3:input_size}, ${4:hidden_size}, bias=${5:True})
```

## Normalization Layer

Creates a normalization layer

<!-- pytorch-layer-norm -->

```python
${1:norm} = nn.${2|BatchNorm1d(num_features\, eps=1e-5\, momentum=0.1\, affine=True\, track_running_stats=True),BatchNorm2d(num_features\, eps=1e-5\, momentum=0.1\, affine=True\, track_running_stats=True),BatchNorm3d(num_features\, eps=1e-5\, momentum=0.1\, affine=True\, track_running_stats=True),GroupNorm(num_groups\, num_channels\, eps=1e-5\, affine=True),SyncBatchNorm(num_features\, eps=1e-05\, momentum=0.1\, affine=True),InstanceNorm1d(num_features\, eps=1e-5\, momentum=0.1\, affine=False\, track_running_stats=False),InstanceNorm2d(num_features\, eps=1e-5\, momentum=0.1\, affine=False\, track_running_stats=False),InstanceNorm3d(num_features\, eps=1e-5\, momentum=0.1\, affine=False\, track_running_stats=False),LayerNorm(normalized_shape\, eps=1e-5\, elementwise_affine=True),LocalResponseNorm(size\, alpha=1e-4\, beta=0.75\, k=1)|}
```

## Linear Layer

Creates a linear layer

<!-- pytorch-layer-linear -->

```python
${1:linear} = nn.${2|Identity(,Linear(in_feature\, ,Bilinear(in_features1\, in_features2\, |}out_features, bias=True)
```

## Dropout

Adds dropout

<!-- pytorch-layer-dropout -->

```python
${1:drop} = nn.${2|Dropout,Dropout2d,Dropout3d,AlphaDropout|}(p=${3:0.5}, inplace=${4|False,True|})
```

## Sparse Layer

Creates a sparse layer

<!-- pytorch-layer-sparse -->

```python
${1:sparse} = nn.${2|Embedding,EmbeddingBag|}(${3:num_embeddings}, ${4:embedding_dim})
```

## Vision Layer

Creates a vision layer

<!-- pytorch-layer-vision -->

```python
${1:vision} = nn.${2|PixelShuffle(upscale_factor),Upsample(size=None\, scale_factor=None\, mode='nearest'\, align_corners=None),UpsamplingNearest2d(size=None\, scale_factor=None),UpsamplingBilinear2d(size=None\, scale_factor=None)|}
```

## Distance Layer

Creates a distance layer

<!-- pytorch-layer-distance -->

```python
${1:distance} = nn.${2|CosineSimilarity,PairwiseDistance|}()
```

## Activation Function

Applies a nonlinearity function

<!-- pytorch-F-activation -->

```python
F.${1|threshold(input\, threshold\, value\, inplace=False),relu(input\, inplace=False),relu6(input\, inplace=False),hardtanh(input\, min_val=-1.\, max_val=1.\, inplace=False),elu(input\, alpha=1.0\, inplace=False),selu(input\, inplace=False),celu(input\, alpha=1.\, inplace=False),leaky_relu(input\, negative_slope=0.01\, inplace=False),prelu(input\, weight),rrelu(input\, lower=1./8\, upper=1./3\, training=False\, inplace=False),glu(input\, dim=-1),logsigmoid(input),hardshrink(input\, lambd=0.5),tanhshrink(input),softsign(input),softplus(input\, beta=1\, threshold=20),softmin(input\, dim=None\, _stacklevel=3),softmax(input\, dim=None\, _stacklevel=3),softshrink(input\, lambd=0.5),gumbel_softmax(logits\, tau=1\, hard=False\, eps=1e-10),log_softmax(input\, dim=None\, _stacklevel=3),tanh(input),sigmoid(input)|}
```

## Convolution Function

Applies a convolution function

<!-- pytorch-F-conv -->

```python
F.${1|conv1d,conv2d,conv3d,conv_transpose1d,conv_transpose2d,conv_transpose3d|}(${2:input}, ${3:weight}, bias=None, stride=1, padding=0)
```

## Pooling Function

Applies a pooling function

<!-- pytorch-F-pooling -->

```python
F.${1|avg_pool1d(input\, kernel_size\, stride=None\, padding=0),avg_pool2d(input\, kernel_size\, stride=None\, padding=0),avg_pool3d(input\, kernel_size\, stride=None\, padding=0),max_pool1d(input\, kernel_size\, stride=None\, padding=0),max_pool2d(input\, kernel_size\, stride=None\, padding=0,max_pool3d(input\, kernel_size\, stride=None\, padding=0),max_unpool1d(input\, indices\, kernel_size\, stride=None\, padding=0),max_unpool2d(input\, indices\, kernel_size\, stride=None\, padding=0),max_unpool3d(input\, indices\, kernel_size\, stride=None\, padding=0),lp_pool1d(input\, norm_type\, kernel_size\, stride=None),lp_pool2d(input\, norm_type\, kernel_size\, stride=None),adaptive_max_pool1d(input\, output_size),adaptive_max_pool2d(input\, output_size),adaptive_max_pool3d(input\, output_size),adaptive_avg_pool1d(input\, output_size),adaptive_avg_pool2d(input\, output_size),adaptive_avg_pool3d(input\, output_size)|}
```

## Normalization Function

Applies a normalization function

<!-- pytorch-F-norm -->

```python
F.${1|batch_norm(input\, running_mean\, running_var),instance_norm(input\, running_mean=None\, running_var=None),layer_norm(input\, normalized_shape),local_response_norm(input\, size),normalize(input)|}
```

## Linear Function

Applies a linear function

<!-- pytorch-F-linear -->

```python
F.${1|linear(input\, weight),bilinear(input1\, input2\, weight)|}
```

## Dropout Function

Applies a dropout function

<!-- pytorch-F-dropout -->

```python
F.${1|dropout,dropout2d,dropout3d,alpha_dropout|}(${2:input}, p=${3:0.5})
```

## Sparse Function

Applies an embedding function

<!-- pytorch-F-sparse -->

```python
F.${1|embedding,embedding_bag|}(${2:input}, ${3:weight})
```

## One Hot Encoding

Applies an one hot encoding function

<!-- pytorch-F-one_hot -->

```python
F.one_hot(${1:tensor}, num_classes=${2:0})
```

## Distance Function

Applies a distance function

<!-- pytorch-F-distance -->

```python
F.${1|pairwise_distance,cosine_similarity|}(${2:x1}, ${3:x2})
```

## Vision Function

Applies a vision function

<!-- pytorch-F-vision -->

```python
F.${1|pixel_shuffle(input\, upscale_factor),pad(input\, pad),interpolate(input\, size=None\, scale_factor=None\, mode='nearest'\, align_corners=None),grid_sample(input\, grid),affine_grid(theta\, size)|}
```

## Loss Function

Applies a loss function

<!-- pytorch-F-loss -->

```python
F.${1|cross_entropy,binary_cross_entropy,binary_cross_entropy_with_logits,poisson_nll_loss,hinge_embedding_loss,kl_div,l1_loss,smooth_l1_loss,mse_loss,multilabel_margin_loss,multilabel_soft_margin_loss,multi_margin_loss,nll_loss,soft_margin_loss|}(${2:input}, ${3:target})
```

## Resnet Basic Block

Creates a Resnet basic block

<!-- pytorch-layer-resnet-block -->

```python
class BasicBlock(nn.Module):
	# see https://pytorch.org/docs/0.4.0/_modules/torchvision/models/resnet.html
	def __init__(self, inplanes, planes, stride=1):
		super(BasicBlock, self).__init__()
		self.conv1 = nn.Conv2d(inplanes, planes, kernel_size=3, stride=stride, padding=1, bias=False)
		self.bn1 = nn.BatchNorm2d(planes)
		self.relu = nn.ReLU(inplace=True)
		self.conv2 = nn.Conv2d(planes, planes, kernel_size=3, padding=1, bias=False)
		self.bn2 = nn.BatchNorm2d(planes)

	def forward(self, x):
		residual = x
		out = self.conv1(x)
		out = self.bn1(out)
		out = self.relu(out)
		out = self.conv2(out)
		out = self.bn2(out)
		out += residual
		out = self.relu(out)
		return out
```

## Resnet Bottleneck Block

Creates a Resnet bottleneck block

<!-- pytorch-layer-resnet-bottleneck -->

```python
class Bottleneck(nn.Module):
	# see https://pytorch.org/docs/0.4.0/_modules/torchvision/models/resnet.html 
	def __init__(self, inplanes, planes, stride=1, downsample=None):
		super(Bottleneck, self).__init__()
		self.conv1 = nn.Conv2d(inplanes, planes, kernel_size=1, stride=stride, bias=False)
		self.bn1 = nn.BatchNorm2d(planes)
		self.conv2 = nn.Conv2d(planes, planes, kernel_size=3, stride=1, padding=1, bias=False)
		self.bn2 = nn.BatchNorm2d(planes)
		self.conv3 = nn.Conv2d(planes, planes * 4, kernel_size=1, bias=False)
		self.bn3 = nn.BatchNorm2d(planes * 4)
		self.relu = nn.ReLU(inplace=True)

	def forward(self, x):
		residual = x
		out = self.conv1(x)
		out = self.bn1(out)
		out = self.relu(out)
		out = self.conv2(out)
		out = self.bn2(out)
		out = self.relu(out)
		out = self.conv3(out)
		out = self.bn3(out)
		out += residual
		out = self.relu(out)
		return out
```

## Imagenet Example

Imagenet code example

<!-- pytorch-examples-imagenet -->

```python
import argparse
import os
import random
import shutil
import time
import warnings

import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.distributed as dist
import torch.optim
import torch.multiprocessing as mp
import torch.utils.data
import torch.utils.data.distributed
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torchvision.models as models

model_names = sorted(name for name in models.__dict__
	if name.islower() and not name.startswith("__")
	and callable(models.__dict__[name]))

parser = argparse.ArgumentParser(description='PyTorch ImageNet Training')
parser.add_argument('data', metavar='DIR',
					help='path to dataset')
parser.add_argument('-a', '--arch', metavar='ARCH', default='resnet18',
					choices=model_names,
					help='model architecture: ' +
						' | '.join(model_names) +
						' (default: resnet18)')
parser.add_argument('-j', '--workers', default=4, type=int, metavar='N',
					help='number of data loading workers (default: 4)')
parser.add_argument('--epochs', default=90, type=int, metavar='N',
					help='number of total epochs to run')
parser.add_argument('--start-epoch', default=0, type=int, metavar='N',
					help='manual epoch number (useful on restarts)')
parser.add_argument('-b', '--batch-size', default=256, type=int,
					metavar='N',
					help='mini-batch size (default: 256), this is the total '
						 'batch size of all GPUs on the current node when '
						 'using Data Parallel or Distributed Data Parallel')
parser.add_argument('--lr', '--learning-rate', default=0.1, type=float,
					metavar='LR', help='initial learning rate', dest='lr')
parser.add_argument('--momentum', default=0.9, type=float, metavar='M',
					help='momentum')
parser.add_argument('--wd', '--weight-decay', default=1e-4, type=float,
					metavar='W', help='weight decay (default: 1e-4)',
					dest='weight_decay')
parser.add_argument('-p', '--print-freq', default=10, type=int,
					metavar='N', help='print frequency (default: 10)')
parser.add_argument('--resume', default='', type=str, metavar='PATH',
					help='path to latest checkpoint (default: none)')
parser.add_argument('-e', '--evaluate', dest='evaluate', action='store_true',
					help='evaluate model on validation set')
parser.add_argument('--pretrained', dest='pretrained', action='store_true',
					help='use pre-trained model')
parser.add_argument('--world-size', default=-1, type=int,
					help='number of nodes for distributed training')
parser.add_argument('--rank', default=-1, type=int,
					help='node rank for distributed training')
parser.add_argument('--dist-url', default='tcp://224.66.41.62:23456', type=str,
					help='url used to set up distributed training')
parser.add_argument('--dist-backend', default='nccl', type=str,
					help='distributed backend')
parser.add_argument('--seed', default=None, type=int,
					help='seed for initializing training. ')
parser.add_argument('--gpu', default=None, type=int,
					help='GPU id to use.')
parser.add_argument('--multiprocessing-distributed', action='store_true',
					help='Use multi-processing distributed training to launch '
						 'N processes per node, which has N GPUs. This is the '
						 'fastest way to use PyTorch for either single node or '
						 'multi node data parallel training')

best_acc1 = 0


def main():
	args = parser.parse_args()

	if args.seed is not None:
		random.seed(args.seed)
		torch.manual_seed(args.seed)
		cudnn.deterministic = True
		warnings.warn('You have chosen to seed training. '
					  'This will turn on the CUDNN deterministic setting, '
					  'which can slow down your training considerably! '
					  'You may see unexpected behavior when restarting '
					  'from checkpoints.')

	if args.gpu is not None:
		warnings.warn('You have chosen a specific GPU. This will completely '
					  'disable data parallelism.')

	if args.dist_url == "env://" and args.world_size == -1:
		args.world_size = int(os.environ["WORLD_SIZE"])

	args.distributed = args.world_size > 1 or args.multiprocessing_distributed

	ngpus_per_node = torch.cuda.device_count()
	if args.multiprocessing_distributed:
		# Since we have ngpus_per_node processes per node, the total world_size
		# needs to be adjusted accordingly
		args.world_size = ngpus_per_node * args.world_size
		# Use torch.multiprocessing.spawn to launch distributed processes: the
		# main_worker process function
		mp.spawn(main_worker, nprocs=ngpus_per_node, args=(ngpus_per_node, args))
	else:
		# Simply call main_worker function
		main_worker(args.gpu, ngpus_per_node, args)


def main_worker(gpu, ngpus_per_node, args):
	global best_acc1
	args.gpu = gpu

	if args.gpu is not None:
		print("Use GPU: {} for training".format(args.gpu))

	if args.distributed:
		if args.dist_url == "env://" and args.rank == -1:
			args.rank = int(os.environ["RANK"])
		if args.multiprocessing_distributed:
			# For multiprocessing distributed training, rank needs to be the
			# global rank among all the processes
			args.rank = args.rank * ngpus_per_node + gpu
		dist.init_process_group(backend=args.dist_backend, init_method=args.dist_url,
								world_size=args.world_size, rank=args.rank)
	# create model
	if args.pretrained:
		print("=> using pre-trained model '{}'".format(args.arch))
		model = models.__dict__[args.arch](pretrained=True)
	else:
		print("=> creating model '{}'".format(args.arch))
		model = models.__dict__[args.arch]()

	if args.distributed:
		# For multiprocessing distributed, DistributedDataParallel constructor
		# should always set the single device scope, otherwise,
		# DistributedDataParallel will use all available devices.
		if args.gpu is not None:
			torch.cuda.set_device(args.gpu)
			model.cuda(args.gpu)
			# When using a single GPU per process and per
			# DistributedDataParallel, we need to divide the batch size
			# ourselves based on the total number of GPUs we have
			args.batch_size = int(args.batch_size / ngpus_per_node)
			args.workers = int((args.workers + ngpus_per_node - 1) / ngpus_per_node)
			model = torch.nn.parallel.DistributedDataParallel(model, device_ids=[args.gpu])
		else:
			model.cuda()
			# DistributedDataParallel will divide and allocate batch_size to all
			# available GPUs if device_ids are not set
			model = torch.nn.parallel.DistributedDataParallel(model)
	elif args.gpu is not None:
		torch.cuda.set_device(args.gpu)
		model = model.cuda(args.gpu)
	else:
		# DataParallel will divide and allocate batch_size to all available GPUs
		if args.arch.startswith('alexnet') or args.arch.startswith('vgg'):
			model.features = torch.nn.DataParallel(model.features)
			model.cuda()
		else:
			model = torch.nn.DataParallel(model).cuda()

	# define loss function (criterion) and optimizer
	criterion = nn.CrossEntropyLoss().cuda(args.gpu)

	optimizer = torch.optim.SGD(model.parameters(), args.lr,
								momentum=args.momentum,
								weight_decay=args.weight_decay)

	# optionally resume from a checkpoint
	if args.resume:
		if os.path.isfile(args.resume):
			print("=> loading checkpoint '{}'".format(args.resume))
			checkpoint = torch.load(args.resume)
			args.start_epoch = checkpoint['epoch']
			best_acc1 = checkpoint['best_acc1']
			if args.gpu is not None:
				# best_acc1 may be from a checkpoint from a different GPU
				best_acc1 = best_acc1.to(args.gpu)
			model.load_state_dict(checkpoint['state_dict'])
			optimizer.load_state_dict(checkpoint['optimizer'])
			print("=> loaded checkpoint '{}' (epoch {})"
				  .format(args.resume, checkpoint['epoch']))
		else:
			print("=> no checkpoint found at '{}'".format(args.resume))

	cudnn.benchmark = True

	# Data loading code
	traindir = os.path.join(args.data, 'train')
	valdir = os.path.join(args.data, 'val')
	normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
								     std=[0.229, 0.224, 0.225])

	train_dataset = datasets.ImageFolder(
		traindir,
		transforms.Compose([
			transforms.RandomResizedCrop(224),
			transforms.RandomHorizontalFlip(),
			transforms.ToTensor(),
			normalize,
		]))

	if args.distributed:
		train_sampler = torch.utils.data.distributed.DistributedSampler(train_dataset)
	else:
		train_sampler = None

	train_loader = torch.utils.data.DataLoader(
		train_dataset, batch_size=args.batch_size, shuffle=(train_sampler is None),
		num_workers=args.workers, pin_memory=True, sampler=train_sampler)

	val_loader = torch.utils.data.DataLoader(
		datasets.ImageFolder(valdir, transforms.Compose([
			transforms.Resize(256),
			transforms.CenterCrop(224),
			transforms.ToTensor(),
			normalize,
		])),
		batch_size=args.batch_size, shuffle=False,
		num_workers=args.workers, pin_memory=True)

	if args.evaluate:
		validate(val_loader, model, criterion, args)
		return

	for epoch in range(args.start_epoch, args.epochs):
		if args.distributed:
			train_sampler.set_epoch(epoch)
		adjust_learning_rate(optimizer, epoch, args)

		# train for one epoch
		train(train_loader, model, criterion, optimizer, epoch, args)

		# evaluate on validation set
		acc1 = validate(val_loader, model, criterion, args)

		# remember best acc@1 and save checkpoint
		is_best = acc1 > best_acc1
		best_acc1 = max(acc1, best_acc1)

		if not args.multiprocessing_distributed or (args.multiprocessing_distributed
				and args.rank % ngpus_per_node == 0):
			save_checkpoint({
				'epoch': epoch + 1,
				'arch': args.arch,
				'state_dict': model.state_dict(),
				'best_acc1': best_acc1,
				'optimizer' : optimizer.state_dict(),
			}, is_best)


def train(train_loader, model, criterion, optimizer, epoch, args):
	batch_time = AverageMeter('Time', ':6.3f')
	data_time = AverageMeter('Data', ':6.3f')
	losses = AverageMeter('Loss', ':.4e')
	top1 = AverageMeter('Acc@1', ':6.2f')
	top5 = AverageMeter('Acc@5', ':6.2f')
	progress = ProgressMeter(
		len(train_loader),
		[batch_time, data_time, losses, top1, top5],
		prefix="Epoch: [{}]".format(epoch))

	# switch to train mode
	model.train()

	end = time.time()
	for i, (images, target) in enumerate(train_loader):
		# measure data loading time
		data_time.update(time.time() - end)

		if args.gpu is not None:
			images = images.cuda(args.gpu, non_blocking=True)
		target = target.cuda(args.gpu, non_blocking=True)

		# compute output
		output = model(images)
		loss = criterion(output, target)

		# measure accuracy and record loss
		acc1, acc5 = accuracy(output, target, topk=(1, 5))
		losses.update(loss.item(), images.size(0))
		top1.update(acc1[0], images.size(0))
		top5.update(acc5[0], images.size(0))

		# compute gradient and do SGD step
		optimizer.zero_grad()
		loss.backward()
		optimizer.step()

		# measure elapsed time
		batch_time.update(time.time() - end)
		end = time.time()

		if i % args.print_freq == 0:
			progress.display(i)


def validate(val_loader, model, criterion, args):
	batch_time = AverageMeter('Time', ':6.3f')
	losses = AverageMeter('Loss', ':.4e')
	top1 = AverageMeter('Acc@1', ':6.2f')
	top5 = AverageMeter('Acc@5', ':6.2f')
	progress = ProgressMeter(
		len(val_loader),
		[batch_time, losses, top1, top5],
		prefix='Test: ')

	# switch to evaluate mode
	model.eval()

	with torch.no_grad():
		end = time.time()
		for i, (images, target) in enumerate(val_loader):
			if args.gpu is not None:
				images = images.cuda(args.gpu, non_blocking=True)
			target = target.cuda(args.gpu, non_blocking=True)

			# compute output
			output = model(images)
			loss = criterion(output, target)

			# measure accuracy and record loss
			acc1, acc5 = accuracy(output, target, topk=(1, 5))
			losses.update(loss.item(), images.size(0))
			top1.update(acc1[0], images.size(0))
			top5.update(acc5[0], images.size(0))

			# measure elapsed time
			batch_time.update(time.time() - end)
			end = time.time()

			if i % args.print_freq == 0:
				progress.display(i)

		# TODO: this should also be done with the ProgressMeter
		print(' * Acc@1 {top1.avg:.3f} Acc@5 {top5.avg:.3f}'
			  .format(top1=top1, top5=top5))

	return top1.avg


def save_checkpoint(state, is_best, filename='checkpoint.pth.tar'):
	torch.save(state, filename)
	if is_best:
		shutil.copyfile(filename, 'model_best.pth.tar')


class AverageMeter(object):
	"""Computes and stores the average and current value"""
	def __init__(self, name, fmt=':f'):
		self.name = name
		self.fmt = fmt
		self.reset()

	def reset(self):
		self.val = 0
		self.avg = 0
		self.sum = 0
		self.count = 0

	def update(self, val, n=1):
		self.val = val
		self.sum += val * n
		self.count += n
		self.avg = self.sum / self.count

	def __str__(self):
		fmtstr = '{name} {val' + self.fmt + '} ({avg' + self.fmt + '})'
		return fmtstr.format(**self.__dict__)


class ProgressMeter(object):
	def __init__(self, num_batches, meters, prefix=""):
		self.batch_fmtstr = self._get_batch_fmtstr(num_batches)
		self.meters = meters
		self.prefix = prefix

	def display(self, batch):
		entries = [self.prefix + self.batch_fmtstr.format(batch)]
		entries += [str(meter) for meter in self.meters]
		print('\t'.join(entries))

	def _get_batch_fmtstr(self, num_batches):
		num_digits = len(str(num_batches // 1))
		fmt = '{:' + str(num_digits) + 'd}'
		return '[' + fmt + '/' + fmt.format(num_batches) + ']'


def adjust_learning_rate(optimizer, epoch, args):
	"""Sets the learning rate to the initial LR decayed by 10 every 30 epochs"""
	lr = args.lr * (0.1 ** (epoch // 30))
	for param_group in optimizer.param_groups:
		param_group['lr'] = lr


def accuracy(output, target, topk=(1,)):
	"""Computes the accuracy over the k top predictions for the specified values of k"""
	with torch.no_grad():
		maxk = max(topk)
		batch_size = target.size(0)

		_, pred = output.topk(maxk, 1, True, True)
		pred = pred.t()
		correct = pred.eq(target.view(1, -1).expand_as(pred))

		res = []
		for k in topk:
			correct_k = correct[:k].view(-1).float().sum(0, keepdim=True)
			res.append(correct_k.mul_(100.0 / batch_size))
		return res


if __name__ == '__main__':
	main()
```

## Mnist Example

Mnist code example

<!-- pytorch-examples-mnist -->

```python
from __future__ import print_function
import argparse
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms


class Net(nn.Module):
	def __init__(self):
		super(Net, self).__init__()
		self.conv1 = nn.Conv2d(1, 20, 5, 1)
		self.conv2 = nn.Conv2d(20, 50, 5, 1)
		self.fc1 = nn.Linear(4*4*50, 500)
		self.fc2 = nn.Linear(500, 10)

	def forward(self, x):
		x = F.relu(self.conv1(x))
		x = F.max_pool2d(x, 2, 2)
		x = F.relu(self.conv2(x))
		x = F.max_pool2d(x, 2, 2)
		x = x.view(-1, 4*4*50)
		x = F.relu(self.fc1(x))
		x = self.fc2(x)
		return F.log_softmax(x, dim=1)
   
def train(args, model, device, train_loader, optimizer, epoch):
	model.train()
	for batch_idx, (data, target) in enumerate(train_loader):
		data, target = data.to(device), target.to(device)
		optimizer.zero_grad()
		output = model(data)
		loss = F.nll_loss(output, target)
		loss.backward()
		optimizer.step()
		if batch_idx % args.log_interval == 0:
			print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
				epoch, batch_idx * len(data), len(train_loader.dataset),
				100. * batch_idx / len(train_loader), loss.item()))

def test(args, model, device, test_loader):
	model.eval()
	test_loss = 0
	correct = 0
	with torch.no_grad():
		for data, target in test_loader:
			data, target = data.to(device), target.to(device)
			output = model(data)
			test_loss += F.nll_loss(output, target, reduction='sum').item() # sum up batch loss
			pred = output.argmax(dim=1, keepdim=True) # get the index of the max log-probability
			correct += pred.eq(target.view_as(pred)).sum().item()

	test_loss /= len(test_loader.dataset)

	print('\nTest set: Average loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
		test_loss, correct, len(test_loader.dataset),
		100. * correct / len(test_loader.dataset)))

def main():
	# Training settings
	parser = argparse.ArgumentParser(description='PyTorch MNIST Example')
	parser.add_argument('--batch-size', type=int, default=64, metavar='N',
						help='input batch size for training (default: 64)')
	parser.add_argument('--test-batch-size', type=int, default=1000, metavar='N',
						help='input batch size for testing (default: 1000)')
	parser.add_argument('--epochs', type=int, default=10, metavar='N',
						help='number of epochs to train (default: 10)')
	parser.add_argument('--lr', type=float, default=0.01, metavar='LR',
						help='learning rate (default: 0.01)')
	parser.add_argument('--momentum', type=float, default=0.5, metavar='M',
						help='SGD momentum (default: 0.5)')
	parser.add_argument('--no-cuda', action='store_true', default=False,
						help='disables CUDA training')
	parser.add_argument('--seed', type=int, default=1, metavar='S',
						help='random seed (default: 1)')
	parser.add_argument('--log-interval', type=int, default=10, metavar='N',
						help='how many batches to wait before logging training status')
   
	parser.add_argument('--save-model', action='store_true', default=False,
						help='For Saving the current Model')
	args = parser.parse_args()
	use_cuda = not args.no_cuda and torch.cuda.is_available()

	torch.manual_seed(args.seed)

	device = torch.device("cuda" if use_cuda else "cpu")

	kwargs = {'num_workers': 1, 'pin_memory': True} if use_cuda else {}
	train_loader = torch.utils.data.DataLoader(
		datasets.MNIST('../data', train=True, download=True,
					   transform=transforms.Compose([
						   transforms.ToTensor(),
						   transforms.Normalize((0.1307,), (0.3081,))
					   ])),
		batch_size=args.batch_size, shuffle=True, **kwargs)
	test_loader = torch.utils.data.DataLoader(
		datasets.MNIST('../data', train=False, transform=transforms.Compose([
						   transforms.ToTensor(),
						   transforms.Normalize((0.1307,), (0.3081,))
					   ])),
		batch_size=args.test_batch_size, shuffle=True, **kwargs)


	model = Net().to(device)
	optimizer = optim.SGD(model.parameters(), lr=args.lr, momentum=args.momentum)

	for epoch in range(1, args.epochs + 1):
		train(args, model, device, train_loader, optimizer, epoch)
		test(args, model, device, test_loader)

	if (args.save_model):
		torch.save(model.state_dict(),"mnist_cnn.pt")
	   
if __name__ == '__main__':
	main()
```

## RL Example VPG

VPG code example

<!-- pytorch-examples-vpg -->

```python
import argparse
import gym
import numpy as np
from itertools import count

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Categorical


parser = argparse.ArgumentParser(description='PyTorch REINFORCE example')
parser.add_argument('--gamma', type=float, default=0.99, metavar='G',
					help='discount factor (default: 0.99)')
parser.add_argument('--seed', type=int, default=543, metavar='N',
					help='random seed (default: 543)')
parser.add_argument('--render', action='store_true',
					help='render the environment')
parser.add_argument('--log-interval', type=int, default=10, metavar='N',
					help='interval between training status logs (default: 10)')
args = parser.parse_args()


env = gym.make('CartPole-v1')
env.seed(args.seed)
torch.manual_seed(args.seed)


class Policy(nn.Module):
	def __init__(self):
		super(Policy, self).__init__()
		self.affine1 = nn.Linear(4, 128)
		self.dropout = nn.Dropout(p=0.6)
		self.affine2 = nn.Linear(128, 2)

		self.saved_log_probs = []
		self.rewards = []

	def forward(self, x):
		x = self.affine1(x)
		x = self.dropout(x)
		x = F.relu(x)
		action_scores = self.affine2(x)
		return F.softmax(action_scores, dim=1)


policy = Policy()
optimizer = optim.Adam(policy.parameters(), lr=1e-2)
eps = np.finfo(np.float32).eps.item()


def select_action(state):
	state = torch.from_numpy(state).float().unsqueeze(0)
	probs = policy(state)
	m = Categorical(probs)
	action = m.sample()
	policy.saved_log_probs.append(m.log_prob(action))
	return action.item()


def finish_episode():
	R = 0
	policy_loss = []
	returns = []
	for r in policy.rewards[::-1]:
		R = r + args.gamma * R
		returns.insert(0, R)
	returns = torch.tensor(returns)
	returns = (returns - returns.mean()) / (returns.std() + eps)
	for log_prob, R in zip(policy.saved_log_probs, returns):
		policy_loss.append(-log_prob * R)
	optimizer.zero_grad()
	policy_loss = torch.cat(policy_loss).sum()
	policy_loss.backward()
	optimizer.step()
	del policy.rewards[:]
	del policy.saved_log_probs[:]


def main():
	running_reward = 10
	for i_episode in count(1):
		state, ep_reward = env.reset(), 0
		for t in range(1, 10000):  # Don't infinite loop while learning
			action = select_action(state)
			state, reward, done, _ = env.step(action)
			if args.render:
				env.render()
			policy.rewards.append(reward)
			ep_reward += reward
			if done:
				break

		running_reward = 0.05 * ep_reward + (1 - 0.05) * running_reward
		finish_episode()
		if i_episode % args.log_interval == 0:
			print('Episode {}\tLast reward: {:.2f}\tAverage reward: {:.2f}'.format(
				  i_episode, ep_reward, running_reward))
		if running_reward > env.spec.reward_threshold:
			print("Solved! Running reward is now {} and "
				  "the last episode runs to {} time steps!".format(running_reward, t))
			break


if __name__ == '__main__':
	main()
```

## RL Example Actor-Critic

Actor-Critic code example

<!-- pytorch-examples-ac -->

```python
import argparse
import gym
import numpy as np
from itertools import count
from collections import namedtuple

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Categorical

# Cart Pole

parser = argparse.ArgumentParser(description='PyTorch actor-critic example')
parser.add_argument('--gamma', type=float, default=0.99, metavar='G',
					help='discount factor (default: 0.99)')
parser.add_argument('--seed', type=int, default=543, metavar='N',
					help='random seed (default: 543)')
parser.add_argument('--render', action='store_true',
					help='render the environment')
parser.add_argument('--log-interval', type=int, default=10, metavar='N',
					help='interval between training status logs (default: 10)')
args = parser.parse_args()


env = gym.make('CartPole-v0')
env.seed(args.seed)
torch.manual_seed(args.seed)


SavedAction = namedtuple('SavedAction', ['log_prob', 'value'])


class Policy(nn.Module):
	"""
	implements both actor and critic in one model
	"""
	def __init__(self):
		super(Policy, self).__init__()
		self.affine1 = nn.Linear(4, 128)

		# actor's layer
		self.action_head = nn.Linear(128, 2)

		# critic's layer
		self.value_head = nn.Linear(128, 1)

		# action & reward buffer
		self.saved_actions = []
		self.rewards = []

	def forward(self, x):
		"""
		forward of both actor and critic
		"""
		x = F.relu(self.affine1(x))

		# actor: choses action to take from state s_t
		# by returning probability of each action
		action_prob = F.softmax(self.action_head(x), dim=-1)

		# critic: evaluates being in the state s_t
		state_values = self.value_head(x)

		# return values for both actor and critic as a tupel of 2 values:
		# 1. a list with the probability of each action over the action space
		# 2. the value from state s_t
		return action_prob, state_values


model = Policy()
optimizer = optim.Adam(model.parameters(), lr=3e-2)
eps = np.finfo(np.float32).eps.item()


def select_action(state):
	state = torch.from_numpy(state).float()
	probs, state_value = model(state)

	# create a categorical distribution over the list of probabilities of actions
	m = Categorical(probs)

	# and sample an action using the distribution
	action = m.sample()

	# save to action buffer
	model.saved_actions.append(SavedAction(m.log_prob(action), state_value))

	# the action to take (left or right)
	return action.item()


def finish_episode():
	"""
	Training code. Calcultes actor and critic loss and performs backprop.
	"""
	R = 0
	saved_actions = model.saved_actions
	policy_losses = [] # list to save actor (policy) loss
	value_losses = [] # list to save critic (value) loss
	returns = [] # list to save the true values

	# calculate the true value using rewards returned from the environment
	for r in model.rewards[::-1]:
		# calculate the discounted value
		R = r + args.gamma * R
		returns.insert(0, R)

	returns = torch.tensor(returns)
	returns = (returns - returns.mean()) / (returns.std() + eps)

	for (log_prob, value), R in zip(saved_actions, returns):
		advantage = R - value.item()

		# calculate actor (policy) loss
		policy_losses.append(-log_prob * advantage)

		# calculate critic (value) loss using L1 smooth loss
		value_losses.append(F.smooth_l1_loss(value, torch.tensor([R])))

	# reset gradients
	optimizer.zero_grad()

	# sum up all the values of policy_losses and value_losses
	loss = torch.stack(policy_losses).sum() + torch.stack(value_losses).sum()

	# perform backprop
	loss.backward()
	optimizer.step()

	# reset rewards and action buffer
	del model.rewards[:]
	del model.saved_actions[:]


def main():
	running_reward = 10

	# run inifinitely many episodes
	for i_episode in count(1):

		# reset environment and episode reward
		state = env.reset()
		ep_reward = 0

		# for each episode, only run 9999 steps so that we don't
		# infinite loop while learning
		for t in range(1, 10000):

			# select action from policy
			action = select_action(state)

			# take the action
			state, reward, done, _ = env.step(action)

			if args.render:
				env.render()

			model.rewards.append(reward)
			ep_reward += reward
			if done:
				break

		# update cumulative reward
		running_reward = 0.05 * ep_reward + (1 - 0.05) * running_reward

		# perform backprop
		finish_episode()

		# log results
		if i_episode % args.log_interval == 0:
			print('Episode {}\tLast reward: {:.2f}\tAverage reward: {:.2f}'.format(
				  i_episode, ep_reward, running_reward))

		# check if we have "solved" the cart pole problem
		if running_reward > env.spec.reward_threshold:
			print("Solved! Running reward is now {} and "
				  "the last episode runs to {} time steps!".format(running_reward, t))
			break


if __name__ == '__main__':
	main()
```

## DCGAN Example

DCGAN code example

<!-- pytorch-examples-dcgan -->

```python
from __future__ import print_function
import argparse
import os
import random
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim as optim
import torch.utils.data
import torchvision.datasets as dset
import torchvision.transforms as transforms
import torchvision.utils as vutils


parser = argparse.ArgumentParser()
parser.add_argument('--dataset', required=True, help='cifar10 | lsun | mnist |imagenet | folder | lfw | fake')
parser.add_argument('--dataroot', required=True, help='path to dataset')
parser.add_argument('--workers', type=int, help='number of data loading workers', default=2)
parser.add_argument('--batchSize', type=int, default=64, help='input batch size')
parser.add_argument('--imageSize', type=int, default=64, help='the height / width of the input image to network')
parser.add_argument('--nz', type=int, default=100, help='size of the latent z vector')
parser.add_argument('--ngf', type=int, default=64)
parser.add_argument('--ndf', type=int, default=64)
parser.add_argument('--niter', type=int, default=25, help='number of epochs to train for')
parser.add_argument('--lr', type=float, default=0.0002, help='learning rate, default=0.0002')
parser.add_argument('--beta1', type=float, default=0.5, help='beta1 for adam. default=0.5')
parser.add_argument('--cuda', action='store_true', help='enables cuda')
parser.add_argument('--ngpu', type=int, default=1, help='number of GPUs to use')
parser.add_argument('--netG', default='', help="path to netG (to continue training)")
parser.add_argument('--netD', default='', help="path to netD (to continue training)")
parser.add_argument('--outf', default='.', help='folder to output images and model checkpoints')
parser.add_argument('--manualSeed', type=int, help='manual seed')
parser.add_argument('--classes', default='bedroom', help='comma separated list of classes for the lsun data set')

opt = parser.parse_args()
print(opt)

try:
	os.makedirs(opt.outf)
except OSError:
	pass

if opt.manualSeed is None:
	opt.manualSeed = random.randint(1, 10000)
print("Random Seed: ", opt.manualSeed)
random.seed(opt.manualSeed)
torch.manual_seed(opt.manualSeed)

cudnn.benchmark = True

if torch.cuda.is_available() and not opt.cuda:
	print("WARNING: You have a CUDA device, so you should probably run with --cuda")

if opt.dataset in ['imagenet', 'folder', 'lfw']:
	# folder dataset
	dataset = dset.ImageFolder(root=opt.dataroot,
							   transform=transforms.Compose([
								   transforms.Resize(opt.imageSize),
								   transforms.CenterCrop(opt.imageSize),
								   transforms.ToTensor(),
								   transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
							   ]))
	nc=3
elif opt.dataset == 'lsun':
	classes = [ c + '_train' for c in opt.classes.split(',')]
	dataset = dset.LSUN(root=opt.dataroot, classes=classes,
						transform=transforms.Compose([
							transforms.Resize(opt.imageSize),
							transforms.CenterCrop(opt.imageSize),
							transforms.ToTensor(),
							transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
						]))
	nc=3
elif opt.dataset == 'cifar10':
	dataset = dset.CIFAR10(root=opt.dataroot, download=True,
						   transform=transforms.Compose([
							   transforms.Resize(opt.imageSize),
							   transforms.ToTensor(),
							   transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
						   ]))
	nc=3

elif opt.dataset == 'mnist':
		dataset = dset.MNIST(root=opt.dataroot, download=True,
						   transform=transforms.Compose([
							   transforms.Resize(opt.imageSize),
							   transforms.ToTensor(),
							   transforms.Normalize((0.5,), (0.5,)),
						   ]))
		nc=1

elif opt.dataset == 'fake':
	dataset = dset.FakeData(image_size=(3, opt.imageSize, opt.imageSize),
							transform=transforms.ToTensor())
	nc=3

assert dataset
dataloader = torch.utils.data.DataLoader(dataset, batch_size=opt.batchSize,
								         shuffle=True, num_workers=int(opt.workers))

device = torch.device("cuda:0" if opt.cuda else "cpu")
ngpu = int(opt.ngpu)
nz = int(opt.nz)
ngf = int(opt.ngf)
ndf = int(opt.ndf)


# custom weights initialization called on netG and netD
def weights_init(m):
	classname = m.__class__.__name__
	if classname.find('Conv') != -1:
		m.weight.data.normal_(0.0, 0.02)
	elif classname.find('BatchNorm') != -1:
		m.weight.data.normal_(1.0, 0.02)
		m.bias.data.fill_(0)


class Generator(nn.Module):
	def __init__(self, ngpu):
		super(Generator, self).__init__()
		self.ngpu = ngpu
		self.main = nn.Sequential(
			# input is Z, going into a convolution
			nn.ConvTranspose2d(     nz, ngf * 8, 4, 1, 0, bias=False),
			nn.BatchNorm2d(ngf * 8),
			nn.ReLU(True),
			# state size. (ngf*8) x 4 x 4
			nn.ConvTranspose2d(ngf * 8, ngf * 4, 4, 2, 1, bias=False),
			nn.BatchNorm2d(ngf * 4),
			nn.ReLU(True),
			# state size. (ngf*4) x 8 x 8
			nn.ConvTranspose2d(ngf * 4, ngf * 2, 4, 2, 1, bias=False),
			nn.BatchNorm2d(ngf * 2),
			nn.ReLU(True),
			# state size. (ngf*2) x 16 x 16
			nn.ConvTranspose2d(ngf * 2,     ngf, 4, 2, 1, bias=False),
			nn.BatchNorm2d(ngf),
			nn.ReLU(True),
			# state size. (ngf) x 32 x 32
			nn.ConvTranspose2d(    ngf,      nc, 4, 2, 1, bias=False),
			nn.Tanh()
			# state size. (nc) x 64 x 64
		)

	def forward(self, input):
		if input.is_cuda and self.ngpu > 1:
			output = nn.parallel.data_parallel(self.main, input, range(self.ngpu))
		else:
			output = self.main(input)
		return output


netG = Generator(ngpu).to(device)
netG.apply(weights_init)
if opt.netG != '':
	netG.load_state_dict(torch.load(opt.netG))
print(netG)


class Discriminator(nn.Module):
	def __init__(self, ngpu):
		super(Discriminator, self).__init__()
		self.ngpu = ngpu
		self.main = nn.Sequential(
			# input is (nc) x 64 x 64
			nn.Conv2d(nc, ndf, 4, 2, 1, bias=False),
			nn.LeakyReLU(0.2, inplace=True),
			# state size. (ndf) x 32 x 32
			nn.Conv2d(ndf, ndf * 2, 4, 2, 1, bias=False),
			nn.BatchNorm2d(ndf * 2),
			nn.LeakyReLU(0.2, inplace=True),
			# state size. (ndf*2) x 16 x 16
			nn.Conv2d(ndf * 2, ndf * 4, 4, 2, 1, bias=False),
			nn.BatchNorm2d(ndf * 4),
			nn.LeakyReLU(0.2, inplace=True),
			# state size. (ndf*4) x 8 x 8
			nn.Conv2d(ndf * 4, ndf * 8, 4, 2, 1, bias=False),
			nn.BatchNorm2d(ndf * 8),
			nn.LeakyReLU(0.2, inplace=True),
			# state size. (ndf*8) x 4 x 4
			nn.Conv2d(ndf * 8, 1, 4, 1, 0, bias=False),
			nn.Sigmoid()
		)

	def forward(self, input):
		if input.is_cuda and self.ngpu > 1:
			output = nn.parallel.data_parallel(self.main, input, range(self.ngpu))
		else:
			output = self.main(input)

		return output.view(-1, 1).squeeze(1)


netD = Discriminator(ngpu).to(device)
netD.apply(weights_init)
if opt.netD != '':
	netD.load_state_dict(torch.load(opt.netD))
print(netD)

criterion = nn.BCELoss()

fixed_noise = torch.randn(opt.batchSize, nz, 1, 1, device=device)
real_label = 1
fake_label = 0

# setup optimizer
optimizerD = optim.Adam(netD.parameters(), lr=opt.lr, betas=(opt.beta1, 0.999))
optimizerG = optim.Adam(netG.parameters(), lr=opt.lr, betas=(opt.beta1, 0.999))

for epoch in range(opt.niter):
	for i, data in enumerate(dataloader, 0):
		############################
		# (1) Update D network: maximize log(D(x)) + log(1 - D(G(z)))
		###########################
		# train with real
		netD.zero_grad()
		real_cpu = data[0].to(device)
		batch_size = real_cpu.size(0)
		label = torch.full((batch_size,), real_label, device=device)

		output = netD(real_cpu)
		errD_real = criterion(output, label)
		errD_real.backward()
		D_x = output.mean().item()

		# train with fake
		noise = torch.randn(batch_size, nz, 1, 1, device=device)
		fake = netG(noise)
		label.fill_(fake_label)
		output = netD(fake.detach())
		errD_fake = criterion(output, label)
		errD_fake.backward()
		D_G_z1 = output.mean().item()
		errD = errD_real + errD_fake
		optimizerD.step()

		############################
		# (2) Update G network: maximize log(D(G(z)))
		###########################
		netG.zero_grad()
		label.fill_(real_label)  # fake labels are real for generator cost
		output = netD(fake)
		errG = criterion(output, label)
		errG.backward()
		D_G_z2 = output.mean().item()
		optimizerG.step()

		print('[%d/%d][%d/%d] Loss_D: %.4f Loss_G: %.4f D(x): %.4f D(G(z)): %.4f / %.4f'
			  % (epoch, opt.niter, i, len(dataloader),
				 errD.item(), errG.item(), D_x, D_G_z1, D_G_z2))
		if i % 100 == 0:
			vutils.save_image(real_cpu,
					'%s/real_samples.png' % opt.outf,
					normalize=True)
			fake = netG(fixed_noise)
			vutils.save_image(fake.detach(),
					'%s/fake_samples_epoch_%03d.png' % (opt.outf, epoch),
					normalize=True)

	# do checkpointing
	torch.save(netG.state_dict(), '%s/netG_epoch_%d.pth' % (opt.outf, epoch))
	torch.save(netD.state_dict(), '%s/netD_epoch_%d.pth' % (opt.outf, epoch))
```

## Variational Autoencoder Example

Variational autoencoder code example

<!-- pytorch-examples-vae -->

```python
from __future__ import print_function
import argparse
import torch
import torch.utils.data
from torch import nn, optim
from torch.nn import functional as F
from torchvision import datasets, transforms
from torchvision.utils import save_image


parser = argparse.ArgumentParser(description='VAE MNIST Example')
parser.add_argument('--batch-size', type=int, default=128, metavar='N',
					help='input batch size for training (default: 128)')
parser.add_argument('--epochs', type=int, default=10, metavar='N',
					help='number of epochs to train (default: 10)')
parser.add_argument('--no-cuda', action='store_true', default=False,
					help='enables CUDA training')
parser.add_argument('--seed', type=int, default=1, metavar='S',
					help='random seed (default: 1)')
parser.add_argument('--log-interval', type=int, default=10, metavar='N',
					help='how many batches to wait before logging training status')
args = parser.parse_args()
args.cuda = not args.no_cuda and torch.cuda.is_available()

torch.manual_seed(args.seed)

device = torch.device("cuda" if args.cuda else "cpu")

kwargs = {'num_workers': 1, 'pin_memory': True} if args.cuda else {}
train_loader = torch.utils.data.DataLoader(
	datasets.MNIST('../data', train=True, download=True,
				   transform=transforms.ToTensor()),
	batch_size=args.batch_size, shuffle=True, **kwargs)
test_loader = torch.utils.data.DataLoader(
	datasets.MNIST('../data', train=False, transform=transforms.ToTensor()),
	batch_size=args.batch_size, shuffle=True, **kwargs)


class VAE(nn.Module):
	def __init__(self):
		super(VAE, self).__init__()

		self.fc1 = nn.Linear(784, 400)
		self.fc21 = nn.Linear(400, 20)
		self.fc22 = nn.Linear(400, 20)
		self.fc3 = nn.Linear(20, 400)
		self.fc4 = nn.Linear(400, 784)

	def encode(self, x):
		h1 = F.relu(self.fc1(x))
		return self.fc21(h1), self.fc22(h1)

	def reparameterize(self, mu, logvar):
		std = torch.exp(0.5*logvar)
		eps = torch.randn_like(std)
		return mu + eps*std

	def decode(self, z):
		h3 = F.relu(self.fc3(z))
		return torch.sigmoid(self.fc4(h3))

	def forward(self, x):
		mu, logvar = self.encode(x.view(-1, 784))
		z = self.reparameterize(mu, logvar)
		return self.decode(z), mu, logvar


model = VAE().to(device)
optimizer = optim.Adam(model.parameters(), lr=1e-3)


# Reconstruction + KL divergence losses summed over all elements and batch
def loss_function(recon_x, x, mu, logvar):
	BCE = F.binary_cross_entropy(recon_x, x.view(-1, 784), reduction='sum')

	# see Appendix B from VAE paper:
	# Kingma and Welling. Auto-Encoding Variational Bayes. ICLR, 2014
	# https://arxiv.org/abs/1312.6114
	# 0.5 * sum(1 + log(sigma^2) - mu^2 - sigma^2)
	KLD = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp())

	return BCE + KLD


def train(epoch):
	model.train()
	train_loss = 0
	for batch_idx, (data, _) in enumerate(train_loader):
		data = data.to(device)
		optimizer.zero_grad()
		recon_batch, mu, logvar = model(data)
		loss = loss_function(recon_batch, data, mu, logvar)
		loss.backward()
		train_loss += loss.item()
		optimizer.step()
		if batch_idx % args.log_interval == 0:
			print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
				epoch, batch_idx * len(data), len(train_loader.dataset),
				100. * batch_idx / len(train_loader),
				loss.item() / len(data)))

	print('====> Epoch: {} Average loss: {:.4f}'.format(
		  epoch, train_loss / len(train_loader.dataset)))


def test(epoch):
	model.eval()
	test_loss = 0
	with torch.no_grad():
		for i, (data, _) in enumerate(test_loader):
			data = data.to(device)
			recon_batch, mu, logvar = model(data)
			test_loss += loss_function(recon_batch, data, mu, logvar).item()
			if i == 0:
				n = min(data.size(0), 8)
				comparison = torch.cat([data[:n],
								      recon_batch.view(args.batch_size, 1, 28, 28)[:n]])
				save_image(comparison.cpu(),
						 'results/reconstruction_' + str(epoch) + '.png', nrow=n)

	test_loss /= len(test_loader.dataset)
	print('====> Test set loss: {:.4f}'.format(test_loss))

if __name__ == "__main__":
	for epoch in range(1, args.epochs + 1):
		train(epoch)
		test(epoch)
		with torch.no_grad():
			sample = torch.randn(64, 20).to(device)
			sample = model.decode(sample).cpu()
			save_image(sample.view(64, 1, 28, 28),
					   'results/sample_' + str(epoch) + '.png')
```
