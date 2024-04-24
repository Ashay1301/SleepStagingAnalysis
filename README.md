# SleepStagingAnalysis
Deep Neural Model for Automated Sleep Staging System using Single-Channel EEG Signal
Introduced a CNN-LSTM network for automated sleep staging using single-channel EEG signals. The model
addresses data imbalance and achieves high classification performance on a healthy population dataset. It
combines CNN for feature learning, LSTM for time information, and achieves an average test accuracy of
91.12%


An efficient deep learning model for sleep stage scoring based on raw, single-channel EEG.
[[paper](https://link.springer.com/chapter/10.1007/978-981-19-6525-8_6)]




## Model Architecture
![TinySleepNet](./img/tinysleepnet.png)
Note: Fs is the sampling rate of the input EEG signals

## Performance Comparison
![Performance Comparison](./img/compare_performance.png)
Note: ACC = accuracy, MF1 = Macro F1-Score


## Environment

* CUDA 10.0
* cuDNN 7
* Tensorflow 1.13.1

## Create a virtual environment with conda

```bash
conda create -n sleepstaging python=3.6
conda activate sleepstaging
pip install -r requirements.txt
```

## How to run

1. `python download_sleepedf.py`
1. `python prepare_sleepedf.py`
1. `python trainer.py --db sleepedf --gpu 0 --from_fold 0 --to_fold 19`
1. `python predict.py --config_file config/sleepedf.py --model_dir out_sleepedf/train --output_dir out_sleepedf/predict --log_file out_sleepedf/predict.log --use-best`


## Licence
- For academic and non-commercial use only
- Apache License 2.0
