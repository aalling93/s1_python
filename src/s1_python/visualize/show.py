import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import requests
from matplotlib import rc
from PIL import Image


def show_thumbnail_function(
    gpd, amount: int = 60, username: str = "", password: str = ""
):
    """ """
    if (len(gpd)) < amount:
        amount = len(gpd)

    fig, axs = plt.subplots(
        int(amount / 5) + 1,
        5,
        figsize=(25, int(amount + 5)),
        facecolor="w",
        edgecolor="k",
    )
    fig.subplots_adjust(hspace=0.5, wspace=0.001)
    axs = axs.ravel()

    for i in range(amount):
        try:
            link = gpd.link_icon.iloc[i]
            im = Image.open(
                requests.get(link, stream=True, auth=(username, password)).raw
            )
            axs[i].imshow(im)
            axs[i].set_title(f"Img {i}")
        except:
            pass

    plt.show()


def show_co_pol_function(gpd, amount: int = 60, username: str = "", password: str = ""):
    """ """
    if (len(gpd)) < amount:
        amount = len(gpd)

    fig, axs = plt.subplots(
        int(amount / 5) + 1,
        5,
        figsize=(25, int(amount + 5)),
        facecolor="w",
        edgecolor="k",
    )
    fig.subplots_adjust(hspace=0.5, wspace=0.001)
    axs = axs.ravel()

    for i in range(amount):
        try:
            link = gpd.link_icon.iloc[i]
            im = np.array(
                Image.open(
                    requests.get(link, stream=True, auth=(username, password)).raw
                )
            )

            axs[i].imshow(im[:, :, 0], cmap="gray")
            axs[i].set_title(f"Img {i}")
        except:
            pass

    plt.show()


def show_cross_pol_function(
    gpd, amount: int = 60, username: str = "", password: str = ""
):
    """ """
    if (len(gpd)) < amount:
        amount = len(gpd)

    fig, axs = plt.subplots(
        int(amount / 5) + 1,
        5,
        figsize=(25, int(amount + 5)),
        facecolor="w",
        edgecolor="k",
    )
    fig.subplots_adjust(hspace=0.5, wspace=0.001)
    axs = axs.ravel()

    for i in range(amount):
        try:
            link = gpd.link_icon.iloc[i]
            im = np.array(
                Image.open(
                    requests.get(link, stream=True, auth=(username, password)).raw
                )
            )

            axs[i].imshow(im[:, :, 1], cmap="gray")
            axs[i].set_title(f"Img {i}")
        except:
            pass

    plt.show()



def initi(size: int = 32):
    matplotlib.rcParams.update({"font.size": size})
    rc("font", **{"family": "sans-serif", "sans-serif": ["Helvetica"]})
    rc("font", **{"family": "serif", "serif": ["Palatino"]})
    rc("text", usetex=True)
