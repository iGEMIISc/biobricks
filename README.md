# Using LLMs to Improve the Descriptions of Biobricks Registry Entries

![](https://raw.githubusercontent.com/iGEMIISc/biobricks/master/parts%20versus%20description%20lengths.png)

Description lengths in the above plot are in terms of number of characters. It can be observed that a significant number of parts have very short descriptions. For now, we hypothesise that the quality of a description is directly proportional to its length.

## Experimental Setup

We choose registry parts with descriptions of length upto 4 characters. There are 708 such parts. We will use our model to generate better descriptions for these parts. To fine-tune our model, we select parts with good descriptions. In accordance with our hypothesis, we choose parts with descriptions of length greater than 80 characters. There are 758 such parts. We will use these parts to fine-tune our model.
