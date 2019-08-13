# About EvoSim

EvoSim is a general purpose 2D evolution simulation package. Generalized creatures called "blobs" are created and seek out generalized "food" elements to keep from starving. If they have enough food, they will reproduce and generate a new, identical blob creature.

## Implemented Features

- The simulation is scalable to any number of blob creatures, food objects, and map sizes.
- Blob Creatures have complete knowledge of food locations (mediated by the SimController) and seek out the closest food element with perfect efficiency.
- Food objects have variable nutrition value that ranges from 0.9 to 1.1 (currently hard-coded). This nutrition is converted to fuel in the blob creatures at perfect efficiency (1-to-1 ratio), (mediated by SimController). When food is removed, the SimController places a new food object at a random location on the map.
- When blobs eat sufficient food to reproduce (parameter is hard-coded in SimController.blobs_multi), they will pause for some number of time-steps (hard-coded in SimController.blobs_multi) and produce an identical blob offspring.
- All position data of blobs and food, along with blob fuel levels and food value levels, are written to a CSV file.

## Known Bugs & Planned Features

### Known Bugs

- CSV reading and writing will be changed entirely to better account for variable numbers of blob creatures. Current animate method handles this okay, but doesn't have the flexibility to change individual blob and food object parameters (like size or color) to reflect simulation values.

### Planned Features

- Blobs will carry genetic material that will change slowly with time, introducing zeroth-order Darwinian competition as an element of the simulation. The genetic material will be saved as a DNA object and will control blob parameters, like move speed and the hunger modifier.
- Blobs will be able to reproduce sexually, using a combination of two partial DNA sets, instead of asexually. This will be a toggleable option
- All parameters, (hunger, move speed, reproduction fuel cost, food-to-fuel efficiency, etc.) will be tunable parameters and will not be hard-coded in hard-to-find parts of the code. They may be read in from a config file.
- Food placement will have parameters that will change the placement distribution. It will also have options to make placement non-random.
- Emergence of cannibalism/carnivorism as a food source will be implemented.
- Neural Network control of blob creatures will be added. Planned package for NN development is PyTorch.
- Multi-processing solutions may be added to increase simulation speed. Numba JIT compilation for high-impact methods is also planned.

## Class Summaries

- SimContoller Class: Interface that runs the simulation. This class is responsible for creating, deleting, updating, and modifying all simulation objects. Current simulation objects include blob creatures and food elements.
- Blob Class: Objects have x and y positions, a "fuel" counter, and internal hunger modifier parameters. Their "move" method is called by SimController to update their position internally based on passed parameters derived from food location parameters.
- Food Class: Objects have x and y positions, and a "value" parameter. They are fixed and do not evolve with time. Their food value is called by SimContoller and passed to the Blob creature that eats it. The food is converted to fuel at a 1-to-1 ratio.
- Animate Method: Separate from the simulation objects, the Animate Method reads in a simulation data file from the 'data/' directory and creates a 2D animation using the FuncAnimate class from matplotlib.
