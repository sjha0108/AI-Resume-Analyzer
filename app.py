import time
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.add_vertical_space import add_vertical_space
from PyPDF2 import PdfReader
from groq import Groq
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import warnings
warnings.filterwarnings('ignore')


def streamlit_config():
    st.set_page_config(page_title='Resume Analyzer AI', layout="wide")
    page_background_color = """
    <style>
    [data-testid="stHeader"] { background: rgba(0,0,0,0); }
    </style>
    """
    st.markdown(page_background_color, unsafe_allow_html=True)
    st.markdown('<h1 style="text-align: center;">Resume Analyzer AI</h1>', unsafe_allow_html=True)


class resume_analyzer:

    def pdf_to_text(pdf):
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text

    def call_gemini(gemini_api_key, text, prompt):
        client = Groq(api_key=gemini_api_key)
        full_prompt = f"{prompt}\n\nResume Content:\n{text[:8000]}"
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": full_prompt}]
        )
        return response.choices[0].message.content

    def resume_summary():
        with st.form(key="Summary"):
            add_vertical_space(1)
            pdf = st.file_uploader(label="Upload Your Resume", type="pdf")
            add_vertical_space(1)
            col1, col2 = st.columns([0.6, 0.4])
            with col1:
                gemini_api_key = st.text_input(label="Enter Groq API Key", type="password")
            add_vertical_space(2)
            submit = st.form_submit_button(label="Submit")
            add_vertical_space(1)
        add_vertical_space(3)
        if submit:
            if pdf is not None and gemini_api_key != "":
                try:
                    with st.spinner("Processing..."):
                        text = resume_analyzer.pdf_to_text(pdf)
                        prompt = "Please provide a detailed summarization of the below resume and conclude with key highlights."
                        summary = resume_analyzer.call_gemini(gemini_api_key, text, prompt)
                    st.markdown("<h4 style=\"color: orange;\">Summary:</h4>", unsafe_allow_html=True)
                    st.write(summary)
                except Exception as e:
                    st.markdown(f"<h5 style=\"text-align: center;color: orange;\">{e}</h5>", unsafe_allow_html=True)
            elif pdf is None:
                st.markdown("<h5 style=\"text-align: center;color: orange;\">Please Upload Your Resume</h5>", unsafe_allow_html=True)
            elif gemini_api_key == "":
                st.markdown("<h5 style=\"text-align: center;color: orange;\">Please Enter Gemini API Key</h5>", unsafe_allow_html=True)

    def resume_strength():
        with st.form(key="Strength"):
            add_vertical_space(1)
            pdf = st.file_uploader(label="Upload Your Resume", type="pdf")
            add_vertical_space(1)
            col1, col2 = st.columns([0.6, 0.4])
            with col1:
                gemini_api_key = st.text_input(label="Enter Groq API Key", type="password")
            add_vertical_space(2)
            submit = st.form_submit_button(label="Submit")
            add_vertical_space(1)
        add_vertical_space(3)
        if submit:
            if pdf is not None and gemini_api_key != "":
                try:
                    with st.spinner("Processing..."):
                        text = resume_analyzer.pdf_to_text(pdf)
                        prompt = "Please provide a detailed analysis of the STRENGTHS of this resume. What makes it stand out?"
                        strength = resume_analyzer.call_gemini(gemini_api_key, text, prompt)
                    st.markdown("<h4 style=\"color: orange;\">Strength:</h4>", unsafe_allow_html=True)
                    st.write(strength)
                except Exception as e:
                    st.markdown(f"<h5 style=\"text-align: center;color: orange;\">{e}</h5>", unsafe_allow_html=True)
            elif pdf is None:
                st.markdown("<h5 style=\"text-align: center;color: orange;\">Please Upload Your Resume</h5>", unsafe_allow_html=True)

    def resume_weakness():
        with st.form(key="Weakness"):
            add_vertical_space(1)
            pdf = st.file_uploader(label="Upload Your Resume", type="pdf")
            add_vertical_space(1)
            col1, col2 = st.columns([0.6, 0.4])
            with col1:
                gemini_api_key = st.text_input(label="Enter Groq API Key", type="password")
            add_vertical_space(2)
            submit = st.form_submit_button(label="Submit")
            add_vertical_space(1)
        add_vertical_space(3)
        if submit:
            if pdf is not None and gemini_api_key != "":
                try:
                    with st.spinner("Processing..."):
                        text = resume_analyzer.pdf_to_text(pdf)
                        prompt = "Please provide a detailed analysis of the WEAKNESSES of this resume and specific suggestions to improve it."
                        weakness = resume_analyzer.call_gemini(gemini_api_key, text, prompt)
                    st.markdown("<h4 style=\"color: orange;\">Weakness and Suggestions:</h4>", unsafe_allow_html=True)
                    st.write(weakness)
                except Exception as e:
                    st.markdown(f"<h5 style=\"text-align: center;color: orange;\">{e}</h5>", unsafe_allow_html=True)
            elif pdf is None:
                st.markdown("<h5 style=\"text-align: center;color: orange;\">Please Upload Your Resume</h5>", unsafe_allow_html=True)

    def job_title_suggestion():
        with st.form(key="Job Titles"):
            add_vertical_space(1)
            pdf = st.file_uploader(label="Upload Your Resume", type="pdf")
            add_vertical_space(1)
            col1, col2 = st.columns([0.6, 0.4])
            with col1:
                gemini_api_key = st.text_input(label="Enter Groq API Key", type="password")
            add_vertical_space(2)
            submit = st.form_submit_button(label="Submit")
            add_vertical_space(1)
        add_vertical_space(3)
        if submit:
            if pdf is not None and gemini_api_key != "":
                try:
                    with st.spinner("Processing..."):
                        text = resume_analyzer.pdf_to_text(pdf)
                        prompt = "Based on this resume, what are the most suitable job titles this person should apply for on LinkedIn? List them with brief explanations."
                        job_title = resume_analyzer.call_gemini(gemini_api_key, text, prompt)
                    st.markdown("<h4 style=\"color: orange;\">Job Titles:</h4>", unsafe_allow_html=True)
                    st.write(job_title)
                except Exception as e:
                    st.markdown(f"<h5 style=\"text-align: center;color: orange;\">{e}</h5>", unsafe_allow_html=True)
            elif pdf is None:
                st.markdown("<h5 style=\"text-align: center;color: orange;\">Please Upload Your Resume</h5>", unsafe_allow_html=True)


class linkedin_scraper:

    def webdriver_setup():
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        return driver

    def get_userinput():
        add_vertical_space(2)
        with st.form(key="linkedin_scarp"):
            add_vertical_space(1)
            col1, col2, col3 = st.columns([0.5, 0.3, 0.2], gap="medium")
            with col1:
                job_title_input = st.text_input(label="Job Title")
                job_title_input = job_title_input.split(",")
            with col2:
                job_location = st.text_input(label="Job Location", value="India")
            with col3:
                job_count = st.number_input(label="Job Count", min_value=1, value=1, step=1)
            add_vertical_space(1)
            submit = st.form_submit_button(label="Submit")
            add_vertical_space(1)
        return job_title_input, job_location, job_count, submit

    def build_url(job_title, job_location):
        b = []
        for i in job_title:
            x = i.split()
            y = "%20".join(x)
            b.append(y)
        job_title = "%2C%20".join(b)
        link = f"https://in.linkedin.com/jobs/search?keywords={job_title}&location={job_location}&locationId=&geoId=102713980&f_TPR=r604800&position=1&pageNum=0"
        return link

    def open_link(driver, link):
        while True:
            try:
                driver.get(link)
                driver.implicitly_wait(5)
                time.sleep(3)
                driver.find_element(by=By.CSS_SELECTOR, value="span.switcher-tabs__placeholder-text.m-auto")
                return
            except NoSuchElementException:
                continue

    def link_open_scrolldown(driver, link, job_count):
        linkedin_scraper.open_link(driver, link)
        for i in range(0, job_count):
            body = driver.find_element(by=By.TAG_NAME, value="body")
            body.send_keys(Keys.PAGE_UP)
            try:
                driver.find_element(by=By.CSS_SELECTOR,
                    value="button[data-tracking-control-name='public_jobs_contextual-sign-in-modal_modal_dismiss']>icon>svg").click()
            except:
                pass
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            driver.implicitly_wait(2)
            try:
                driver.find_element(by=By.CSS_SELECTOR, value="button[aria-label='See more jobs']").click()
                driver.implicitly_wait(5)
            except:
                pass

    def job_title_filter(scrap_job_title, user_job_title_input):
        user_input = [i.lower().strip() for i in user_job_title_input]
        scrap_title = [i.lower().strip() for i in [scrap_job_title]]
        confirmation_count = 0
        for i in user_input:
            if all(j in scrap_title[0] for j in i.split()):
                confirmation_count += 1
        return scrap_job_title if confirmation_count > 0 else np.nan

    def scrap_company_data(driver, job_title_input, job_location):
        company = driver.find_elements(by=By.CSS_SELECTOR, value="h4[class=\"base-search-card__subtitle\"]")
        company_name = [i.text for i in company]
        location = driver.find_elements(by=By.CSS_SELECTOR, value="span[class=\"job-search-card__location\"]")
        company_location = [i.text for i in location]
        title = driver.find_elements(by=By.CSS_SELECTOR, value="h3[class=\"base-search-card__title\"]")
        job_title = [i.text for i in title]
        url = driver.find_elements(by=By.XPATH, value="//a[contains(@href, \"/jobs/\")]")
        website_url = [i.get_attribute("href") for i in url]
        df = pd.DataFrame(company_name, columns=["Company Name"])
        df["Job Title"] = pd.DataFrame(job_title)
        df["Location"] = pd.DataFrame(company_location)
        df["Website URL"] = pd.DataFrame(website_url)
        df["Job Title"] = df["Job Title"].apply(lambda x: linkedin_scraper.job_title_filter(x, job_title_input))
        df["Location"] = df["Location"].apply(lambda x: x if job_location.lower() in x.lower() else np.nan)
        df = df.dropna()
        df.reset_index(drop=True, inplace=True)
        return df

    def scrap_job_description(driver, df, job_count):
        website_url = df["Website URL"].tolist()
        job_description = []
        description_count = 0
        for i in range(0, len(website_url)):
            try:
                linkedin_scraper.open_link(driver, website_url[i])
                driver.find_element(by=By.CSS_SELECTOR, value="button[data-tracking-control-name=\"public_jobs_show-more-html-btn\"]").click()
                driver.implicitly_wait(5)
                time.sleep(1)
                description = driver.find_elements(by=By.CSS_SELECTOR, value="div[class=\"show-more-less-html__markup relative overflow-hidden\"]")
                data = [i.text for i in description][0]
                if len(data.strip()) > 0 and data not in job_description:
                    job_description.append(data)
                    description_count += 1
                else:
                    job_description.append("Description Not Available")
            except:
                job_description.append("Description Not Available")
            if description_count == job_count:
                break
        df = df.iloc[:len(job_description), :]
        df["Job Description"] = pd.DataFrame(job_description, columns=["Description"])
        df["Job Description"] = df["Job Description"].apply(lambda x: np.nan if x == "Description Not Available" else x)
        df = df.dropna()
        df.reset_index(drop=True, inplace=True)
        return df

    def display_data_userinterface(df_final):
        add_vertical_space(1)
        if len(df_final) > 0:
            for i in range(0, len(df_final)):
                st.markdown(f"<h3 style=\"color: orange;\">Job Posting Details : {i+1}</h3>", unsafe_allow_html=True)
                st.write(f"Company Name : {df_final.iloc[i,0]}")
                st.write(f"Job Title    : {df_final.iloc[i,1]}")
                st.write(f"Location     : {df_final.iloc[i,2]}")
                st.write(f"Website URL  : {df_final.iloc[i,3]}")
                with st.expander(label="Job Description"):
                    st.write(df_final.iloc[i, 4])
                add_vertical_space(3)
        else:
            st.markdown("<h5 style=\"text-align: center;color: orange;\">No Matching Jobs Found</h5>", unsafe_allow_html=True)

    def main():
        driver = None
        try:
            job_title_input, job_location, job_count, submit = linkedin_scraper.get_userinput()
            add_vertical_space(2)
            if submit:
                if job_title_input != [] and job_location != "":
                    with st.spinner("Chrome Webdriver Setup Initializing..."):
                        driver = linkedin_scraper.webdriver_setup()
                    with st.spinner("Loading More Job Listings..."):
                        link = linkedin_scraper.build_url(job_title_input, job_location)
                        linkedin_scraper.link_open_scrolldown(driver, link, job_count)
                    with st.spinner("Scraping Job Details..."):
                        df = linkedin_scraper.scrap_company_data(driver, job_title_input, job_location)
                        df_final = linkedin_scraper.scrap_job_description(driver, df, job_count)
                    linkedin_scraper.display_data_userinterface(df_final)
                elif job_title_input == []:
                    st.markdown("<h5 style=\"text-align: center;color: orange;\">Job Title is Empty</h5>", unsafe_allow_html=True)
                elif job_location == "":
                    st.markdown("<h5 style=\"text-align: center;color: orange;\">Job Location is Empty</h5>", unsafe_allow_html=True)
        except Exception as e:
            add_vertical_space(2)
            st.markdown(f"<h5 style=\"text-align: center;color: orange;\">{e}</h5>", unsafe_allow_html=True)
        finally:
            if driver:
                driver.quit()


streamlit_config()
add_vertical_space(2)

with st.sidebar:
    add_vertical_space(4)
    option = option_menu(menu_title="", options=["Summary", "Strength", "Weakness", "Job Titles", "Linkedin Jobs"],
                         icons=["house-fill", "database-fill", "pass-fill", "list-ul", "linkedin"])

if option == "Summary":
    resume_analyzer.resume_summary()
elif option == "Strength":
    resume_analyzer.resume_strength()
elif option == "Weakness":
    resume_analyzer.resume_weakness()
elif option == "Job Titles":
    resume_analyzer.job_title_suggestion()
elif option == "Linkedin Jobs":
    linkedin_scraper.main()
