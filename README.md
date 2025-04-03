## Manim

Trying out the Manim Community Edition Framework

## Installation

1. `brew update`
2. `brew upgrade`
3. `brew install pango cairo ffmpeg py3cairo pkg-config manim`
4. `pip install -r requirements.txt`

## Rendering

High quality video rendering for producing ready-to-show animations:

`manim --progress_bar display -pqh <FILE_NAME>.py <CLASS_NAME>`

Low quality video rendering for quicker feedback when animating:

`manim --progress_bar display -pql <FILE_NAME>.py <CLASS_NAME>`

Gif rendering (quality limited to avoid performance problems):

`manim --progress_bar --format=gif display -pql <FILE_NAME>.py <CLASS_NAME>`

High quality image rendering of the last frame in the scene:

`manim --progress_bar display -pqh -s <FILE_NAME>.py <CLASS_NAME>`

High quality image rendering of the last frame in the scene with transparent background:

`manim --progress_bar display -pqh -s -t <FILE_NAME>.py <CLASS_NAME>`

In all cases:

- Media will be displayed
- Media will be saved to `./media`
