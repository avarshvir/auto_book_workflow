import asyncio
#import time
from playwright_scrapper.scrap import fetch_chapter
from ai_agents.ai_writer import spin_text
from ai_agents.ai_reviewer import review_text
from pathlib import Path
from versioning.version_store import save_version

DATA_PATH = Path("data")    

def all_function():
    with open(DATA_PATH/"chapter_1.txt", "r", encoding="utf-8") as f:
        original_text = f.read()
        
    print("AI Writer is Running")
    ai_writer_output_text = spin_text(original_text)     #ai writer function
    print("-----AI Writer Ouput-----")
    print(ai_writer_output_text)

    #Human Interaction
    choice = input("Do you want to edit this content? press y for yes and n for no: ")
    if choice == 'y':
        print("----Write your content below----")
        human_text = input()
        ai_writer_output_text = ai_writer_output_text + human_text
        with open(DATA_PATH / "rewrite_chapter.txt", "w", encoding="utf-8") as f:
            f.write(ai_writer_output_text)
    else:
        with open(DATA_PATH / "rewrite_chapter.txt", "w", encoding="utf-8") as f:
            f.write(ai_writer_output_text)



    print("AI Reviewer is Running")
    reviewed = review_text(ai_writer_output_text)        #ai reviewer function
    with open(DATA_PATH / "reviewed_chapter.txt", "w", encoding="utf-8") as f:
        f.write(reviewed)
    
    return reviewed


if __name__ == "__main__":
    print("--------------------")
    asyncio.run(fetch_chapter())
    #time.sleep(20)
    reviewed_text = all_function()
    save_version(reviewed_text, tag="human_loop_1")
