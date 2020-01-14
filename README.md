Link to main paper: [Barack’s Wife Hillary:Using Knowledge Graphs for Fact-Aware Language Modeling](https://rloganiv.github.io/assets/projects/kglm.pdf)
* Code in offical [repo](https://github.com/rloganiv/kglm-model)

Relevant paper to start reproducing: 
* [Dynamic Entity Representations in Neural Language Models](https://www.aclweb.org/anthology/D17-1195.pdf) 
  * Code in official [repo](https://github.com/jiyfeng/entitynlm)
* [A Neural Knowledge Language Model](https://arxiv.org/pdf/1608.00318.pdf)
  * Could not find any repos

Relevant techniques used in main paper:
* COPYNET: [Incorporating Copying Mechanism in Sequence-to-Sequence Learning](https://www.aclweb.org/anthology/P16-1154.pdf)
  * Possible [repo](https://github.com/mjc92/CopyNet) with pytorch code 

Relevant data sources/ preparations used in the paper:
* Wikidata: [Denny Vrandeciˇ c and Markus Krötzsch. 2014. ´ Wikidata: A free collaborative knowledgebase. Communications of the ACM, 57(10):78–85.](https://rloganiv.github.io/assets/projects/kglm.pdf#page=9&zoom=100,402,477)

* Entity linker to identify additional links to Wikipedia (only first time a entity is mentioned on a wikipage the link to another wikipage will be made): [Entity Linking via Joint Encoding of Types, Descriptions, and Context](https://cogcomp.seas.upenn.edu/papers/GuptaSiRo17.pdf)

* Identify Coreferences on wikipedia using Standford CoreNLP: https://stanfordnlp.github.io/CoreNLP/

Download the PROCESSED data (linked-wikitext-2) containing 268MB from https://github.com/rloganiv/kglm-model
Put in the data-folder into your repo named "linked-wikitext-2" or name it "data". If you name the folder anything else and its in the repo, remember to add it to the .gitignore!

Create a virtualenvironment:
python3 -m virtualenv .env
or 
virtualenv .env
