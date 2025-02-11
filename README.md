## Manim˚

Trying out the Manim Community Edition Framework

## Installation

1. `brew update`
2. `brew upgrade`
3. `brew install pango cairo ffmpeg py3cairo pkg-config`
4. `pip install -r requirements.txt`

## Rendering

High quality rendering for producing ready-to-show animations:

`manim --progress_bar display -pqh <FILE_NAME>.py <CLASS_NAME>`

Low quality rendering for quicker feedback when animating:

`manim --progress_bar display -pql <FILE_NAME>.py <CLASS_NAME>`

In both cases:
- Media will be played
- Media will be saved to `./media`
