"""complete path of the file to read"""
inputfile = "fortest"
matrixInfo = "matrixInfo"
authorIdIndex = "authorIdIndex"
docIdIndex = "docIdIndex"

f_input = open(inputfile, 'r')

f_matrixInfo = open(matrixInfo, 'w')
f_authorIdIndex = open(authorIdIndex, 'w')
f_docIdIndex = open(docIdIndex, 'w')

f_matrixInfo.write("\'index of author\' \'index of doc\' 1 \n\n")
f_authorIdIndex.write("\'author_id\' \'author_index\'\n")
f_docIdIndex.write("\'doc_id\' \'doc_index\' \n")

author_index=0;
doc_index=0;
authors={}
docs={}

for line in f_input:
    nums = [int(x) for x in line.split()]
    (author_id, doc_id, count) = (nums[0:3])
    if( author_id not in authors):
        authors[author_id] = author_index
        """index for next author"""
        author_index += 1
    if( doc_id not in docs):
        docs[doc_id] = doc_index
        """index for next doc"""
        doc_index += 1
    #print author_index-1, doc_index-1, 1
    f_matrixInfo.write("%d %d %d\n" %(author_index-1, doc_index-1, 1))
    
for author in authors:
    f_authorIdIndex.write("%d %d\n" %(author, authors[author]))
    
for doc in docs:
    f_docIdIndex.write("%d %d\n" %(doc, docs[doc]))

    
    
