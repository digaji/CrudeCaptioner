# CrudeCaptioner
This is the greatest Indonesian caption captioning model of All Time

# How to Run
Create and activate the environment
```bash
conda env create -f environment.yml
conda activate tf
```

Download the original dataset
```bash
cd dataset

wget -q https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_Dataset.zip
wget -q https://github.com/jbrownlee/Datasets/releases/download/Flickr8k/Flickr8k_text.zip

unzip -qq Flickr8k_Dataset.zip

mv Flickr8k_text.zip Flicker8k_text
cd Flicker8k_text
unzip -qq Flickr8k_text.zip

rm Flickr8k_text.zip
cd ..
rm Flickr8k_Dataset.zip
```

(optional) Translate the original dataset
```bash
cd dataset

python translator.py
```

Play the Jupyter Notebook
```bash
main.ipynb
```