#By: Anoushka Lakshmi

import cv2 # Imports OpenCV library for image processing 
import re # Imports regular expressuion for pattern finding
import pandas as pd # Imports pandas library for data analysis
import numpy as np  # Imports numpy library for calculations

# Global variables for clicked points, reference distance, and measurements
clicked_points = [] # Stores clicked point coordinates in list
reference_distance = None   # Stores reference distance for 1st two clicks
measurements = []   # Stores measurements in list
legend_entries = [] # Stores legend entries in list

def update_legend():    # Defines function for text in legend   
    global clicked_points, reference_distance, measurements, legend_entries # Global variables 
    legend_text = []    # Makes an empty list for the legend text
    if len(clicked_points) == 2 and reference_distance is None: # Checks if list length of clicked points is 2
        distance_pixels = ((clicked_points[0][0] - clicked_points[1][0])**2 + 
                           (clicked_points[0][1] - clicked_points[1][1])**2)**0.5   # Calculates distance between the 1st 2 clicked points
        reference_distance = distance_pixels    # Defines the reference distance to be the distance between the 1st 2 clicks 
        legend_text = f"Click 1 and 2 = Reference = 1.0 cm" # Writes legend text for reference distance
        legend_entries.append(legend_text)  # Adds the legend text to the legend as an entry
    if len(clicked_points) == 4: # Checks if the number of clicks is equal to 4
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                           (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5 # Calculates the distance between the last and second-to-last point, i.e. clicks 3 and 4
        measurement_cm = (distance_pixels / reference_distance) * 1.0   # Calculates the predicted distance using the reference distance for scaling
        measurements.append(measurement_cm) # Adds the measurement to the measurements list
        legend_text = f"Click 3 and 4 = MC{len(measurements)} = {measurement_cm:.2f} cm"    # Writes legend text for the new measurement obtained
        legend_entries.append(legend_text)  #Adds the legend text to the legend as an entry
    if len(clicked_points) == 6:    # Checks if the number of clicks is equal to 6... (same pattern as before)
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 5 and 6 = P1 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    if len(clicked_points) == 8:
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 7 and 8 = M1 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    if len(clicked_points) == 10:
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 9 and 10 = D1 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    if len(clicked_points) == 12:
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 11 and 12 = MC2 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    if len(clicked_points) == 14:
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 13 and 14 = P2 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    if len(clicked_points) == 16:
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 15 and 16 = M2 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    if len(clicked_points) == 18:
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 17 and 18 = D2 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    if len(clicked_points) == 20:
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 19 and 20 = MC3 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    if len(clicked_points) == 22:
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 21 and 22 = P3 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    if len(clicked_points) == 24:
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 23 and 24 = M3 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    if len(clicked_points) == 26:
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 25 and 26 = D3 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    if len(clicked_points) == 28:
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 27 and 28 = MC4 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    if len(clicked_points) == 30:
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 29 and 30 = P4 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    if len(clicked_points) == 32:
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 31 and 32 = M4 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    if len(clicked_points) == 34:
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 33 and 34 = D4 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    if len(clicked_points) == 36:
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 35 and 36 = MC5 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    if len(clicked_points) == 38:
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 37 and 38 = P5 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    if len(clicked_points) == 40:
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 39 and 40 = D5 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    if len(clicked_points) == 42:
        distance_pixels = ((clicked_points[-1][0] - clicked_points[-2][0])**2 + 
                        (clicked_points[-1][1] - clicked_points[-2][1])**2)**0.5
        measurement_cm = (distance_pixels / reference_distance) * 1.0
        measurements.append(measurement_cm)
        legend_text = f"Click 41 and 42 = W0 = {measurement_cm:.2f} cm"
        legend_entries.append(legend_text)
    return legend_entries   # Ends update function and legend entries provided to functon caller

#Save to excel
def save_measurements_to_excel():   # Defines function to save measurements from legent to Excel file  
    excel_path = r"C:\Users\anous\Downloads\133_subject_prosthetic_measurement_data.xlsx"   # defines path using Excel file path
    df = pd.read_excel(excel_path)  # Stores the read Excel information into dataframe "df"

    column_name = "Gen Left B (cm)"  # Defines Excel column name

    if column_name not in df.columns:   # Checks if column name exists already
        df[column_name] = np.nan    # Adds column using defined column name and populates it with NaN values for later use

    legend_entries = update_legend()    # Assigns variable name "legend_entries" to updated legend
    
    measurement_cms = []    # Defines an empty list for measurement values
    ref_point_removed = False   # Establishes boolean variable using "False"
    for entry in legend_entries: # Goes through entries in legend
        if 'Reference' in entry and not ref_point_removed:  # Checks if reference point in entry
            ref_point_removed = True    # Establishes boolean variable as "True" instead of "False"
        else:   # If reference point not removed:
            match = re.search(r"= (\d+\.\d+)", entry)   # Searches for a decimal following an equal sign in the legend entries
            if match:   # If found:
                measurement_cms.append(float(match.group(1)))   # Adds float data to measurement list
            else:   # If not found:
                measurement_cms.append(np.nan) # Adds "NaN" or not a number to the measurement list

    df[column_name] = measurement_cms   # Adds measurements to specific dataframe column name

    df.to_excel(excel_path, index=False)    # Saves dataframe to specific Excel path without index labels
    print("Values saved to Excel.") # Writes that values were saved to Excel as a checkpoint

def click_event(event, x, y, flags, param): # Defines click event function for callbacks
    global clicked_points, gray_image, legend_entries   # Global variables
    if event == cv2.EVENT_LBUTTONDOWN:  # If left button click occurs:
        clicked_points.append((x, y))   # Adds coordinates of clicked point to list             
        if len(clicked_points) == 44:   # If all measurements are collected, i.e. 44 clicks:
            save_measurements_to_excel()    # Saves measurements to Excel file
            cv2.destroyAllWindows() # Closes OpenCV windows after measurements saved

        else:   # If not all measurements collected:
            legend_image = np.zeros_like(gray_image)    # Creates a black image for depicting legend entries   
            legend_entries = update_legend()    # Updates legend entries as number of clicks increases
            offset = 20 # Spaces legend entries apart vertically
            for i, entry in enumerate(legend_entries):  # Loops through legend entries
                cv2.putText(legend_image, entry, (10, 30 + i * offset), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)  # Defines legend text font, color, thickness
        
            result = cv2.addWeighted(gray_image, 1, legend_image, 0.5, 0)   # Places legend on top of grayscale image
            
            cv2.imshow('Image', result) # Depicts resulting image

image_path = r"C:\Users\anous\Downloads\Left B.jpeg"    # Loads image using file path
image = cv2.imread(image_path)  # Stores read image into variable "image"

if image is None:   # If image not loaded properly:
    print("Error: Unable to load the image.")   # Print statement that image not loaded
else:   # If image is loaded:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)    # Converts image to grayscale
    
    scale_percent = 20  # Resizes image to fit on screen to scaled percentage of 20%
    width = int(gray_image.shape[1] * scale_percent / 100)  # Calculates image width from scaled percentage
    height = int(gray_image.shape[0] * scale_percent / 100) # Calculates image height from scaled percentage
    gray_image = cv2.resize(gray_image, (width, height))    # Depicts resized, grayscaled image
    
    cv2.imshow('Image', gray_image) # Depicts image as grayscale

    cv2.setMouseCallback('Image', click_event)  # Establishes callback function for clicks inside the image

    cv2.waitKey(0)  # Waits with image window open for keyboard input 
    cv2.destroyAllWindows() # Closes all image windows
