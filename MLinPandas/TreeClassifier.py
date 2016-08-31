# TODO: import data from csv


# TODO: create safe_loans column with values +1 for safe loans -1 for risky loans

# TODO: unit test; check imported data


# TODO: create data subset for running classifier


# TODO: unit test; check data subset


# TODO: create training and validation sets from data subset


# TODO: unit test; check correct splitting of training and validation test


# TODO: function: classification error calculator
# Classification-error = # Mistakes / # Total number of data points


# TODOL function: create a leaf node
# Leaf Node Definition: leaf_node = {parent_feature:, left_child: None, right_child: None, class:, depth:}


# TODO: function: interate through all features to find one with least classification error


# TODO: create the root node
# Parent Node Definition: parent_node = {parent_feature: None, left_child:, right_child:, class:, depth:}


# TODO: function: reccursive function to find the stump node and keep splitting until stopping conditions are reached
# Definition: Stopping conditions
    # 1. leaf is reached - all data points belong to the same class
    # 2. max height is reached
    # 3. No more features to split on