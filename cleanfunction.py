import os
import extensition as c
import shutil
def clean():
    number_images = 0
    number_videos = 0
    number_documents = 0
    try :
        rep = input("please entry you folder path : ")

        files = os.listdir(rep)
        types = {
            "images": False,
            "videos": False,
            "documents": False
        }
        file_list = ["images","videos","documents"]
        for name in file_list :
            n =os.path.join(rep , name)
            if not os.path.exists(n):
                    os.makedirs(n,exist_ok=True)
        for f in files :
            if any(f.lower().endswith(i) for i in c.images ):
                types['images']  = True 
                file = os.path.join(rep,f)
                to_file = os.path.join(rep,file_list[0],f)
                shutil.move(file,to_file)
                number_images +=1
            elif any(f.lower().endswith(i) for i in c.videos ):
                types["videos"] = True 
                file = os.path.join(rep,f)
                to_file = os.path.join(rep,file_list[1],f)
                shutil.move(file,to_file)
                number_videos+=1
            elif any(f.lower().endswith(i) for i in c.documents ):
                types["documents"] = True 
                file = os.path.join(rep,f)
                to_file = os.path.join(rep,file_list[2],f)
                shutil.move(file,to_file)
                number_documents+=1

        # for f in files :
        #     if any(f.lower().endswith(ext) for ext in c.images ):
        #         file = os.path.join(rep,f)
        #         to_file = os.path.join(rep,'images',f)
        #         shutil.move(file,to_file)
        #     elif any(f.lower().endswith(ext) for ext in c.videos):
        #         file = os.path.join(rep,f)
        #         to_file = os.path.join(rep,'videos',f)
        #         shutil.move(file,to_file)
        #     elif any(f.lower().endswith(ext) for ext in c.documents):
        #         file = os.path.join(rep,f)
        #         to_file = os.path.join(rep,'documents',f)
        #         shutil.move(file,to_file)
    except FileNotFoundError:
        print(f"Le chemin d’accès spécifié est introuvable: {rep}")

    finally:
        print(f"number of image move to folder (images) is {number_images}")
        print(f"number of video move to folder (videos) is {number_videos}")
        print(f"number of document move to folder (documents) is {number_documents}")

if __name__ == "__main__":
    clean()