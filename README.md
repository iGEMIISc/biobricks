# Using LLMs to Improve the Descriptions of Biobricks Registry Entries

![](https://raw.githubusercontent.com/iGEMIISc/biobricks/master/parts%20versus%20description%20lengths.png)

Description lengths in the above plot are in terms of number of characters. It can be observed that a significant number of parts have very short descriptions. For now, we hypothesise that the quality of a description is directly proportional to its length.

## Experimental Procedure

1. We obtain the complete database of parts from the [iGEM Registry](http://parts.igem.org/fasta/parts/All_Parts) in the form of 24094 FASTA entries. A copy of this database is available [`/parts.txt`](https://raw.githubusercontent.com/iGEMIISc/biobricks/master/parts.txt).

2. We choose registry parts with descriptions of length upto 4 characters. There are 708 such parts. We will use our model to generate better descriptions for these parts. To fine-tune our model, we select parts with good descriptions. In accordance with our hypothesis, we choose parts with descriptions of length greater than 80 characters. There are 758 such parts. We will use these parts to fine-tune our model.

3. For all 1466 parts, we scrape the corresponding part pages (available at `parts.igem.org/Part:{ID}`) and use an LLM to summarize the contents of the page in up to 25 _tokens_.

4. We fine-tune the chosen LLM on the 758 parts with _good descriptions_. Our prompts includes the the type of the part along with the summarized information from its webpage. The target output is the description for that part.

5. We use the fine-tuned LLM to generate descriptions for the 708 parts with _poor descriptions_. Our prompts includes the the type of the part along with the summarized information from its webpage. We generate descriptions with lengths up to 60 _tokens_.

## Results

We used 2 models to produce our results. The first model was `t5-large` and the second model was `google/flan-t5-large` (obtained from HuggingFace). The results from these models are available in [`/output_t5_large.txt`](https://raw.githubusercontent.com/iGEMIISc/biobricks/master/output_t5_large.txt) and [`/output_flan_t5_large.txt`](https://raw.githubusercontent.com/iGEMIISc/biobricks/master/output_flan_t5_large.txt) respectively. Some examples are given below (for the same parts).

### T5-Large

| Part ID | Original Description | Generated Description |
| --- | --- | --- |
| BBa_C0090 | smaI | smaI Coding Region for ahl synthase from serratia sp., <sub>. cerevisiae (Serratia) |
| BBa_C0400 | BglG | BglG is known to bind to terminator loops in bgl operon causing antisepsis. |
| BBa_C0420 | BglF | BglF Sensor permease of bgl operon Sequence and Features Assembly Compatibility%3Answer%3B <i>Bgl%3D |

### Flan-T5-Large

| Part ID | Original Description | Generated Description |
| --- | --- | --- |
| BBa_C0090 | smaI | smaI coding region for AHL synthase smaI from Serratia |
| BBa_C0400 | BglG | BglG is a protein that is known to bind to terminator loops in bgl |
| BBa_C0420 | BglF | BglF Sensor permease of Bgl operon Sequence and Features Assembly Compatibility: |

## Future Work
This repository is work in progress, and the following tasks are planned for the future.

1. Processing scraped data to improve the quality of summaries.
2. Experimenting with more LLMs.
3. Using a larger and more reliable dataset for fine-tuning.
4. Experimenting with prompt-tuning.
5. Experimenting with different prompt formats, and exploring if one-shot or few-shot learning improves results.
6. Exploring reinforcement learning through human feedback. 

## Call for Collaboration

### Labelling
Our hypothesis about the quality of descriptions being directly proportional to their length does not provide a very reliable metric for classification. iGEM teams can work collaboratively to label the parts in the registry as _good_ or _poor_ based on the quality of their descriptions, and this can potentially improve the quality of our dataset. This labelling can also help us set-up a reinforcement learning pipeline.

### Development
Developing this pipeline requires expertise in several areas that we are still learning and exploring. We would love to collaborate with teams that have experience in machine learning, natural language processing and LLMs.

### Integration
We would like to integrate this pipeline with the iGEM Registry, so that once our model generates _good-enough_ results, we can modify the entries in the registry with the new descriptions.

### Evaluation
We would like other iGEM teams to help us in evaluating the results from this pipeline during the several stages of development so that we can track the quality of our model.
