<img src="../images/senecac.gif" alt="Seneca College" height="38" width="349" />

# PRG550 Lab #5

### Assigned Week of June 20, 2022

### Due July 5,6, 2022 (in-lab demonstration)

Lab #5 will give you practice with Jupyter notebooks and provide you with an understanding of the Pandas library.
Pandas will be core foundation tool for the rest course.

You will be required update the skeleton `Lab05-Jupyter-and-Pandas.ipynb` notebook and show that 
you reproduced results from the below tutorials in the notebook:

- [What kind of data does pandas handle](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html)
- [Reading and Writing Data in Pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html)
- [Select subset of data](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html)
- [Create new columns of data](https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html)
- [Calculate summary statistics](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html)
- [Manipulating Text Data](https://pandas.pydata.org/docs/getting_started/intro_tutorials/10_text_data.html)


1. Connect to your Pi using `ssh` from a terminal program on your PC
1. Update your Raspberry Pi's local course repository ([instructions here](../references/Tips_and_Tricks.md#updating-local-course-repository-from-github))
1. Ensure the latest notebook is present
    ```
    ls -al /home/pi/seneca-prg550-2022-spring/labs/Lab05-Jupyter-and-Pandas.ipynb
    ```
1. Copy Lab 5 notebook file to your `workspace` directory in the `labs` sub-directory
    ```
    cp /home/pi/seneca-prg550-2022-spring/labs/Lab05-Jupyter-and-Pandas.ipynb /home/pi/workspace/labs/
    ```
1. Start Jupyter notebook from the `workspace` directory
    ```
    cd /home/pi/workspace
    jupyter notebook --no-browser
    ```
1. In Jupyter, navigate to the `labs` directory and open the `Lab05-Jupyter-and-Pandas.ipynb` notebook
1. Follow remaining instructions in the Lab 5 notebook

Tip: open the tutorial links from your PC's browser to reduce memory usage by the Pi

Refer to [Lecture 6 - Notebook](../lectures/Lecture06-Jupyter-Notes.ipynb) in the course repository for notes on navigating around Jupyter.
