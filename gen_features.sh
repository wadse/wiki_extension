#!/bin/sh

# ./word_align de -d 0 -o _features_0
# ./word_align de -d 1 -o _features_1
# ./combine_features de/train_features_0 de/train_features_1 de/train_features
# ./learn de

# ./word_align bg -d 0 -o _features_0
# ./word_align bg -d 1 -o _features_1
# ./combine_features bg/train_features_0 bg/train_features_1 bg/train_features
# ./learn bg

# ./word_align es -d 0 -o _features_0
# ./word_align es -d 1 -o _features_1
# ./combine_features es/train_features_0 es/train_features_1 es/train_features
# ./learn es

./word_align de -d 0 -o _features_0 -t test
./word_align de -d 1 -o _features_1 -t test
./combine_features de/test_features_0 de/test_features_1 de/test_features

./word_align bg -d 0 -o _features_0 -t test
./word_align bg -d 1 -o _features_1 -t test
./combine_features bg/test_features_0 bg/test_features_1 bg/test_features

./word_align es -d 0 -o _features_0 -t test
./word_align es -d 1 -o _features_1 -t test
./combine_features es/test_features_0 es/test_features_1 es/test_features