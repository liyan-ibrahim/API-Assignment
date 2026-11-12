
# Paintings and Soundscapes

This project uses the Met Museum API and Freesound API to find a painting and play a matching soundscape based on a chosen theme.

## Setup

### 1. Install Requirements

Install the requirements.txt file and run the following command in your terminal:

```bash
python3 -m pip install Pillow
```

- `Pillow` is used to open and display the painting images.


## How to Run

Open the project folder in VS Code and run:

```bash
python3 paintingsAndSound.py
```

The program will:
1. Find a painting from the Met Museum API.
2. Open the painting in an image viewer.
3. Find a matching sound using Freesound.
4. Play the sound automatically while the painting is displayed.

## Changing the Theme

At the top of `paintingsAndSound.py`, change:

```python
theme = "Ocean"
```

To any theme you want, for example:

```python
theme = "Flowers"
```

Save and run the program again.

## APIs Used

- [Met Museum API](https://metmuseum.github.io/)
- [Freesound API](https://freesound.org/docs/api/)
