---
# You can also start simply with 'default'
theme: seriph
# random image from a curated Unsplash collection by Anthony
# like them? see https://unsplash.com/collections/94734566/slidev
background: https://cover.sli.dev
# some information about your slides (markdown enabled)
title: Spotify 1.2M+ Songs
info: |
  ## Intermediate Presentation
  by Mazza Luca, Hoxha Roeld, Masciocchi Andrea

  Learn more at [GitHub](https://github.com/lucamazzza/spoty)
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

# Intermediate Presentation

Spotify 1.2M+ Songs • *Mazza Luca, Hoxha Roeld, Masciocchi Andrea*

<div class="abs-br m-6 text-xl">
  <a href="https://github.com/lucamazzza/spoty" target="_blank" class="slidev-icon-btn">
    <carbon:logo-github />
  </a>
</div>

---
transition: slide-left
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

<img src="./assets/loud_vs_energy.png" width="1000">

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

# Danceability vs Valence 

<img src="./assets/dance_vs_valence.png" width="1000">

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

# Songs Samples 
<br>

🎉 **Happy**: Happy - Pharrell Williams

<audio controls>
  <source src="./assets/Happy.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

😡 **Angry**: Killing in the Name - Rage Against the Machine

<audio controls>
  <source src="./assets/KillingInTheName.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

😢 **Sad**: Someone Like You - Adele

<audio controls>
  <source src="./assets/SomeoneLikeYou.mp3" type="audio/mpeg">
  Your browser does not support the audio element.
</audio>

😌 **Peaceful**: Weightless - Marconi Union

<audio controls>
  <source src="./assets/Weightless.mp3" type="audio/mpeg">
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

# Next Steps  
<br>

* Add popularity dataset
* Analyze some complicated graphs, sampling by *popularity*
* Analyze data by *genre*


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

