import requests
from bs4 import BeautifulSoup

def extract_job_details(linkedin_url):
    # Fetch the webpage content
    response = requests.get(linkedin_url)
    if response.status_code != 200:
        print("Failed to fetch the webpage")
        return None, None, None
    
    # Parse HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract company name, job title
    company_name = soup.find('a', {'class': 'topcard__org-name-link'}).text.strip()
    job_title = soup.find('h1', {'class': 'topcard__title'}).text.strip()

    return [company_name, job_title]

# def create_numbers_document(company_name, job_title):
#     # Open Numbers
#     pyautogui.hotkey('command', 'space')
#     pyautogui.write('Numbers')
#     pyautogui.press('enter')
#     time.sleep(5)  # Wait for Numbers to open

#     # Create a new document
#     pyautogui.hotkey('command', 'n')
#     time.sleep(2)

#     # Input the data
#     pyautogui.write(company_name)
#     pyautogui.press('tab')
#     pyautogui.write(job_title)
#     pyautogui.press('tab')
#     pyautogui.write(description)

    # Save the document (optional)
    # pyautogui.hotkey('command', 's')
    # time.sleep(2)
    # pyautogui.write('job_details')
    # pyautogui.press('enter')

def createFile(company_name, job_title):
    with open('./jobs/jobs.csv', 'a') as file:
        file.write(f'\n{company_name}, {job_title}') 

if __name__ == "__main__":
    linkedin_url = "https://www.linkedin.com/jobs/view/3977081096/?alternateChannel=search&refId=IZedksixrPn%2BX01fWZcYBA%3D%3D&trackingId=PwBHIMDzdw%2FKblS3aYRlrQ%3D%3D"

    company_details = extract_job_details(linkedin_url)

    comma_removed_company_details = []
        
    for detail in company_details:
        comma_removed_company_details.append(detail.replace(',','-'))

    if comma_removed_company_details:
       createFile(comma_removed_company_details[0], comma_removed_company_details[1])
       print("Data successfully extracted and input to csv document.")
    else:
       print("Failed to extract job details to file.")

