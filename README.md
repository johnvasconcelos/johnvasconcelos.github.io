# My academic website

This project is meant to develop and maintain John Vasconcelos's academic website, with valuable information on his professional achievements as well as his academic production and status.

___
## Tecnology

Developed in RStudio as a "Quarto Website".

___
## How to rebuild (or build your own under the same model)

>*This uses GitHub Desktop, which is intuitive and visually more appealing for non-developers.

### 1 Building the website in Quarto

- In RStudio, (must have R and RStudio installed), click File > New Project > New Directory > Quarto Website. This is to set up a new folder to store all your project's files.
- In the "New Project Wizard" dialogue box, give the new directory a name and browse for the location in your computer where you want the new folder to be stored. Click "Create Project". 
- A few default files will be created in the project's folder. Two of them ("index.qmd" and "\_quarto.yml") will be visible in RStudio, and the others in the project's folder.
- Each `.qmd` file will yield a page on the website, so you must create a new `.qmd` file for each page you want to appear on your website. An easy way to do it is, in the folder, making copies of the "index.qmd" file and renaming them after each desired page's name. 
- Follow the above procedure to create "research.qmd", "teaching.qmd" and "cv.qmd", which will correspond, respectively to wepages Research, Teaching and CV. In each `.qmd` you should change the header `title: new page name`, respectively "Research", "Teaching" and "CV", and write in markdown the desired page content.
- In our current example there will be no "About" page, so delete "about.qmd" from the project's folder.

### 2 Publishing the repository

- From [https://desktop.github.com/download/](https://desktop.github.com/download/) install Github Desktop and log in with your Github account (you must have one before continuing)
- Identify the project folder to create a repository from it: file > Add local repository > Identify the folder.
- Publish the repository (it will be visible from your Github account)
- Execute a commit after relevant changes, with a summary title.
- Execute "push origin" to send the changes to Github online

