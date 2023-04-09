import torchvision.datasets as datasets
import torchvision.transforms as transforms

# define the directory containing the images
data_dir = "/path/to/directory"

# define the transformations to be applied to the images
transform = transforms.Compose([
    transforms.Resize((224, 224)),  # resize the images to 224x224
    transforms.ToTensor(),          # convert the images to PyTorch tensors
    transforms.Normalize((0.0, 0.0, 0.0), (1/255, 1/255, 1/255))  # rescale pixel values to [0, 1]
])

# create the dataset
dataset = datasets.ImageFolder(root=data_dir, transform=transform)

# create a dataloader to load the images in batches
dataloader = torch.utils.data.DataLoader(dataset, batch_size=32, shuffle=True)
