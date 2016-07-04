# image-search-engine

This search engine takes an image as input and produce output having 3 best matching images from the set of images .right now it is a personal image search engine but this method can be extended to make a more powerful image search engine .

This search engine search images based on the features of the query image. It does not require any manual tagging of images and then searching image based on tag.
In this engine content based image retrieval method is used . It use a simple but effective image descriptor : the color histogram.
It extract all the images of approximately same color pattern as the query image. It is useful when you want to search for all the images of same place like if you want all the photos of beach.
#CONTENT BASED IMAGE RETRIVEL METHOD

"Content-based" means that the search analyzes the contents of the image rather than the metadata such as keywords, tags, or descriptions associated with the image. The term "content" in this context might refer to colors, shapes, textures, or any other information that can be derived from the image itself. CBIR is desirable because searches that rely purely on metadata are dependent on annotation quality and completeness. 
