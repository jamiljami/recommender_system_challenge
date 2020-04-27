# recommender_system_challenge

An implementation of the Recommender System Challenge by @Sirajology on [Youtube](https://youtu.be/9gBC9R-msAk).

# Overview

This code uses [lightfm](https://github.com/lyst/lightfm) recommender system library to train a hybrid content-based + collaborative algorithm that uses the WARP loss function on a [restaurant](https://archive.ics.uci.edu/ml/datasets/Entree+Chicago+Recommendation+Data) dataset. The entree dataset contains restaurant ratings from 50,000 instances. Once trained, our script prints out recommended entrees for whatever users from the dataset that we choose to terminal.

# Dependencies

* numpy (http://www.numpy.org/)
* scipy (https://www.scipy.org/)
* lightfm (https://github.com/lyst/lightfm)

Install missing dependencies using [pip](https://pip.pypa.io/en/stable/installing/)

# Credits

Credit goes to the [lightfm](https://github.com/lyst/lightfm) team and Siraj Raval. I've merely created a wrapper to make it more readable.
