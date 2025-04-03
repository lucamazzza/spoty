---
# You can also start simply with 'default'
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://cover.sli.dev
# some information about your slides (markdown enabled)
title: Welcome to Slidev
info: |
  ## Slidev Starter Template
  Presentation slides for developers.

  Learn more at [Sli.dev](https://sli.dev)
# apply unocss classes to the current slide
class: text-center

# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: slide-left
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true
# open graph
# seoMeta:
#  ogImage: https://cover.sli.dev
---

# Dataset Presentation

Spotify 1.2M+ Songs • *Mazza Luca, Hoxha Roeld, Masciocchi Andrea*

<div class="abs-br m-6 text-xl">
  <a href="https://github.com/lucamazzza/spoty" target="_blank" class="slidev-icon-btn">
    <carbon:logo-github />
  </a>
</div>

---
transition: fade-out
---

# [Spotify 1.2M+ Songs](https://www.kaggle.com/datasets/rodolfofigueroa/spotify-12m-songs?select=tracks_features.csv)

What does the dataset represent?
<br>
<br>
<br>

- 🎶 **Songs** - Spotify's dataset of 1.2M+ entries (1'204'025)
- 📏 **Row** - Each row represents a song
- 🎤 **Columns** - Each column is a characteristic of the song (24 columns)
- ⏱️ **Time Span**: 1908 - 2020 (Publication Date)
- 🌍**Worldwide** - Songs from all over the world

<br>
<br>
<br>

<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

---
transition: slide-up
level: 2
---

# Interesting Columns
Some interesting columns to analyze

|                                                                        |                                            |
| ---------------------------------------------------------------------- | ------------------------------------------ |
| **Song Name**                                                          | Name of the song                           |
| **Danceability** `float(0,1)`<br>**Energy** `float(0,1)`               | Interesting to compare with eachother      |
| **Loudness** `dB`<br>**Speechiness** `float(0,1)`<br>**Duration** `ms` | Interesting the change over the years      |
| **Publication Date** `DateTime`                                        | Most productive parts of the years         |

Spotify computes danceability, energy, ...  with ML algorithms

---
transition: slide-left
level: 2
---

# Why?
Why is this dataset interesting (to us)?

<br>
<br>
<br>

- Spotify is an every-day use for most of us
- Data Credibility
- Songs from all over the world
- Changes over time on music

<br>
<br>
<br>

<style>
h1 {
  background-color: #2B90B6;
  background-image: linear-gradient(45deg, #4EC5D4 10%, #146b8c 20%);
  background-size: 100%;
  -webkit-background-clip: text;
  -moz-background-clip: text;
  -webkit-text-fill-color: transparent;
  -moz-text-fill-color: transparent;
}
</style>

---
layout: center
class: text-center
---

# Thank you!

[Dataset](https://www.kaggle.com/datasets/rodolfofigueroa/spotify-12m-songs?select=tracks_features.csv) · [GitHub](https://github.com/lucamazzza/spoty)

