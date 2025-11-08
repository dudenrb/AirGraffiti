#!/usr/bin/env python3
"""
Birthday Invitation Video Generator for Nikhil Raj
Creates an animated birthday invitation video with colorful effects
"""

from moviepy import ImageClip, TextClip, CompositeVideoClip
from PIL import Image, ImageDraw
import numpy as np
import os

def create_gradient_background(width, height, color1, color2):
    """Create a gradient background image"""
    img = Image.new('RGB', (width, height), color1)
    draw = ImageDraw.Draw(img)
    
    for i in range(height):
        ratio = i / height
        r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
        g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
        b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
        draw.line([(0, i), (width, i)], fill=(r, g, b))
    
    return np.array(img)

def create_confetti_frame(width, height, num_confetti=100):
    """Create a frame with confetti particles"""
    img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), 
              (255, 0, 255), (0, 255, 255), (255, 128, 0)]
    
    for _ in range(num_confetti):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        color = colors[np.random.randint(0, len(colors))]
        size = np.random.randint(5, 15)
        draw.ellipse([x, y, x+size, y+size], fill=color)
    
    return np.array(img)

def create_birthday_video():
    """Create the complete birthday invitation video"""
    
    # Video settings
    width, height = 1280, 720
    fps = 30
    duration = 10
    
    # Color schemes
    bg_color1 = (138, 43, 226)  # Blue Violet
    bg_color2 = (255, 20, 147)  # Deep Pink
    text_color = 'white'
    
    # Create gradient background
    bg_array = create_gradient_background(width, height, bg_color1, bg_color2)
    background = ImageClip(bg_array, duration=duration)
    
    # Scene 1: Opening - "You're Invited!" (0-3 seconds)
    txt_invited = (TextClip(
                           text="You're Invited!", 
                           font_size=80, 
                           color=text_color,
                           stroke_color='gold',
                           stroke_width=3,
                           duration=3)
                  .with_position('center')
                  .with_start(0))
    
    # Scene 2: Main invitation (3-7 seconds)
    txt_main1 = (TextClip(
                         text="Join us to celebrate", 
                         font_size=50, 
                         color=text_color,
                         duration=4)
                .with_position(('center', 200))
                .with_start(3))
    
    txt_main2 = (TextClip(
                         text="NIKHIL RAJ's", 
                         font_size=90, 
                         color='yellow',
                         stroke_color='red',
                         stroke_width=2,
                         duration=4)
                .with_position(('center', 300))
                .with_start(3))
    
    txt_main3 = (TextClip(
                         text="Birthday Celebration!", 
                         font_size=60, 
                         color=text_color,
                         duration=4)
                .with_position(('center', 450))
                .with_start(3))
    
    # Scene 3: Details (7-10 seconds)
    txt_details1 = (TextClip(
                           text="Get ready for an amazing celebration!", 
                           font_size=40, 
                           color=text_color,
                           duration=3)
                  .with_position(('center', 300))
                  .with_start(7))
    
    txt_details2 = (TextClip(
                           text="Let's make it memorable!", 
                           font_size=40, 
                           color='yellow',
                           duration=3)
                  .with_position(('center', 380))
                  .with_start(7))
    
    # Create confetti overlay
    confetti_array = create_confetti_frame(width, height, 150)
    confetti = ImageClip(confetti_array, duration=duration, is_mask=False)
    
    # Combine all elements
    video = CompositeVideoClip([
        background,
        confetti,
        txt_invited,
        txt_main1,
        txt_main2,
        txt_main3,
        txt_details1,
        txt_details2
    ], size=(width, height))
    
    # Set final duration
    video = video.with_duration(duration)
    
    return video

def main():
    """Main function to generate the video"""
    print("🎬 Creating birthday invitation video for Nikhil Raj...")
    print("⏳ This may take a minute...")
    
    try:
        # Create the video
        video = create_birthday_video()
        
        # Output filename
        output_file = "nikhil_raj_birthday_invitation.mp4"
        
        # Write the video file
        video.write_videofile(
            output_file,
            fps=30,
            codec='libx264',
            audio=False,
            preset='medium',
            threads=4
        )
        
        print(f"\n✅ Video created successfully: {output_file}")
        print(f"📁 Location: {os.path.abspath(output_file)}")
        print(f"⏱️  Duration: 10 seconds")
        print(f"📐 Resolution: 1280x720")
        
    except Exception as e:
        print(f"\n❌ Error creating video: {str(e)}")
        import traceback
        traceback.print_exc()
        raise

if __name__ == "__main__":
    main()
