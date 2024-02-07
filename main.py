import cv2
import pandas as pd
import random
import pickle

from tag_manager import tags


tag = tags()
cap = cv2.VideoCapture(0)

capture_rate = 10

max_number = len(tag.tags) - 1

while True:

    menu = input("1: Nueva_captura\n"
                 "2: Guardar datos\n")


    if menu == "1":
        frames = 0

        tag_index = random.randint(0, max_number)

        word_to_interpret = tag.tags[tag_index]

        print(f"Frase elegida: {word_to_interpret}")

        while True:
            frames +=1
            res, frame = cap.read()

            if not res:
                break

            if frames == capture_rate:

                frame_pd = pd.DataFrame({word_to_interpret: [frame]})

                tag.df = tag.df.append(frame_pd, ignore_index=True)

                frames = 0

            if cv2.waitKey(1) & 0xFF == ord('q'):
                #Paro manual de toma de datos
                break


            cv2.imshow('Hello World', frame)

        cv2.destroyWindow('Hello World')
        cap.release()

    elif menu == "2":

        for column in tag.df.columns:
            # Get the data of the column
            column_data = tag.df[column]

            # Define the pickle file name
            pickle_file_name = f"{column}.pickle"

            # Save the data as pickle
            with open(pickle_file_name, 'wb') as f:
                pickle.dump(column_data, f)

            print(f"Saved column '{column}' as {pickle_file_name}")

        break






