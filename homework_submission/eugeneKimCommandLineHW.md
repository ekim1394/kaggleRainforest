## Homework: Command Line Chipotle

#### Submitting Your Homework

* Create a Markdown file that includes your answers **and** the code you used to arrive at those answers.
* Add this Markdown file to a GitHub repo that you'll use for all of your coursework.
* Submit a link to your repo using the homework submission form.

#### Command Line Tasks

1. Look at the head and the tail of **chipotle.tsv** in the **data** subdirectory of this repo. Think for a minute about how the data is structured. What do you think each column means? What do you think each row means? Tell me! (If you're unsure, look at more of the file contents.)

head chipotle.tsv

order_id is the index. quantity is the amount purchased. item_name is the name of the item. Choice_description has extra description for certain items. item_price is the price of the item. Each row looks like it represents a different order at chipotle.

2. How many orders do there appear to be?

tail chipotle.tsv
There appear to be 1834 orders because that is the final order id.

3. How many lines are in this file?

wc -l chipotle.tsv
4623 lines

4. Which burrito is more popular, steak or chicken?

grep 'Steak Burrito' chipotle.tsv | wc -l
368 Steak Burrito orders
$ grep 'Chicken Burrito' chipotle.tsv | wc -l
553 Chicken Burrito Orders

Chicken Burrito seems to be more popular

5. Do chicken burritos more often have black beans or pinto beans?

grep 'Chicken Burrito' chipotle.tsv | grep 'Black Beans' | wc -l
282 orders

grep 'Chicken Burrito' chipotle.tsv | grep 'Pinto Beans' | wc -l
105 orders

More often people get black beans.

6. Make a list of all of the CSV or TSV files in the DAT8 repo (using a single command). Think about how wildcard characters can help you with this task.

find . -name '\*.csv'
find . -name '\*.tsv'

7. Count the approximate number of occurrences of the word "dictionary" (regardless of case) across all files in the DAT-DC repo.

grep -r 'dictionary' .

8. **Optional:** Use the command line to discover something "interesting" about the Chipotle data. Try using the commands from the "advanced" section!
