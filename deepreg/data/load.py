import os

from deepreg.data.nifti.nifti_grouped_loader import NiftiGroupedDataLoader
from deepreg.data.nifti.nifti_paired_loader import NiftiPairedDataLoader
from deepreg.data.nifti.nifti_unpaired_loader import NiftiUnpairedDataLoader


def get_data_loader(data_config, mode):
    """
    Return the corresponding data loader.
    Can't be placed in the same file of loader interfaces as it causes import cycle.
    :param data_config:
    :param mode:
    :return:
    """
    data_dir = data_config["dir"]

    # set mode
    modes = os.listdir(data_dir)
    if "train" not in modes:
        raise ValueError("training data must be provided, they should be stored under train/")
    if mode == "valid" and mode not in modes:
        # when validation data is not available, use test data instead
        mode = "test"
    if mode not in modes:
        return None

    data_type = data_config["type"]
    labeled = data_config["labeled"]
    sample_label = "sample" if mode == "train" else "all"
    seed = None if mode == "train" else 0

    # sanity check for configs
    if data_type not in ["paired", "unpaired", "grouped"]:
        raise ValueError("data type must be paired / unpaired / grouped")

    if data_config["format"] == "nifti":
        if data_type == "paired":
            moving_image_shape = data_config["moving_image_shape"]
            fixed_image_shape = data_config["fixed_image_shape"]
            return NiftiPairedDataLoader(data_dir_path=os.path.join(data_dir, mode),
                                         labeled=labeled,
                                         sample_label=sample_label,
                                         seed=seed,
                                         moving_image_shape=moving_image_shape,
                                         fixed_image_shape=fixed_image_shape)
        elif data_type == "grouped":
            image_shape = data_config["image_shape"]
            intra_group_prob = data_config["intra_group_prob"]
            intra_group_option = data_config["intra_group_option"]
            sample_image_in_group = data_config["sample_image_in_group"]
            return NiftiGroupedDataLoader(data_dir_path=os.path.join(data_dir, mode),
                                          labeled=labeled,
                                          sample_label=sample_label,
                                          intra_group_prob=intra_group_prob,
                                          intra_group_option=intra_group_option,
                                          sample_image_in_group=sample_image_in_group,
                                          seed=seed,
                                          image_shape=image_shape)
        elif data_type == "unpaired":
            image_shape = data_config["image_shape"]
            return NiftiUnpairedDataLoader(data_dir_path=os.path.join(data_dir, mode),
                                           labeled=labeled,
                                           sample_label=sample_label,
                                           seed=seed,
                                           image_shape=image_shape)
    raise ValueError("Unknown data loader type. \nConfig {}\n".format(data_config))