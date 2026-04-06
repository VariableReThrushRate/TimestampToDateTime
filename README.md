# TimestampToDateTime
This is a simple python script designed to convert from a timestamp in a filename to an image sequence format for Kdenlive.
The timestamp is a proprietary format, expressed as "%m%d%Y_%H%M%S" in Python, and 04052026_230002 to normal people (Month, Day, Year, _, Hour, Minute, Second).
It is primarily meant to convert a large batch of images into an image sequence for use in a video editing program, meant to create timelapses from dynamic image sources.
If demand ever occurs, I can add a version that reads EXIF or something.
