---
# You can also start simply with 'default'
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://cover.sli.dev
# some information about your slides (markdown enabled)
title: Spotify 1.2M+ Songs
info: |
  ## Final Presentation
  by Mazza Luca, Hoxha Roeld, Masciocchi Andrea

  Learn more at [GitHub](https://github.com/lucamazzza/spoty)
# apply unocss classes to the current slide
class: text-center

# https://sli.dev/features/drawing
drawings:
  persist: false
# slide transition: https://sli.dev/guide/animations.html#slide-transitions
transition: fade-out
# enable MDC Syntax: https://sli.dev/features/mdc
mdc: true
# open graph
# seoMeta:
#  ogImage: https://cover.sli.dev
---

# Final Presentation

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

- **Songs** - Spotify's dataset of 1.2M+ entries (1'204'025)
- **Row** - Each row represents a song
- **Columns** - Each column is a characteristic of the song (24 columns)
- **Time Span**: 1908 - 2020 (Publication Date)
- **Worldwide** - Songs from all over the world

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
transition: fade-out
---

# Why?
Why is this dataset interesting (to us)?

<br>
<br>
<br>

- Spotify is an every-day use for most of us
- Data Credibility
- Songs from all over the world
- Changes over time / history on music

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
transition: fade-out
---

# Average Song Duration 

<img src="./assets/avg_song_duration.png" width="1000">

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
transition: slide-left
---

# Loudness vs Energy 

<br>

<img src="./assets/loudness_energy.png" width="600">

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
transition: fade-out 
---

# Songs Samples 
<br>
<br>
<br>

💥 **Loudest Song**: Alarm - Marshmello Remix - *Anne-Marie*, *Marshmello*

<audio controls>
  <source src="./assets/alarm.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>


🤫 **Quietest Song**: The Explaination - *XXXTENTACION*

<audio controls>
  <source src="./assets/theexplaination.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>


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
audio {
    margin: 20px 0;
    width: 100%;
}
</style>

---
transition: slide-left
---

# Danceability vs Valence 

<img src="./assets/danceability_valence.png" width="1000">

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
transition: fade-out
---

# Songs Samples 
<br>

🎉 **Happy**: Merrymaking at My Place - *Calvin Harris*

<audio controls>
  <source src="./assets/merrymaking.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

😡 **Angry**: good day - 21 Savage

<audio controls>
  <source src="./assets/goodday.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

😢 **Sad**: Vault Character - Calvin Harris

<audio controls>
  <source src="./assets/vault.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

😌 **Peaceful**: Leave Before the Lights Come On - *Arctic Monkeys*

<audio controls>
  <source src="./assets/leave.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>


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
audio {
    margin: 20px 0;
    width: 100%;
}
</style>

---
transition: fade-out
---

# Songs by Genre 

<br>

<img src="./assets/genres.png" width="700">

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

