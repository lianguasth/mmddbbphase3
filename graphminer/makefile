UNITTESTFILE = unittest1.undir.txt unittest2.undir.txt unittest3.undir.txt unittest4.undir.txt unittest5.undir.txt

DFILESP1 = soc-Epinions1.txt wiki-Vote.txt

UFILESP2 = as-skitter.ungraph-75000.txt com-amazon.ungraph-75000.txt email-Enron.ungraph.txt com-dblp.ungraph-75000.txt
DFILESP2 = cit-HepPh.txt cit-HepTh.txt p2p-Gnutella31.txt ca-AstroPh.txt email-EuAll.txt soc-Slashdot0811-75000.txt

UFILESP3 = as-skitter.ungraph-75000.txt com-amazon.ungraph-75000.txt email-Enron.ungraph.txt com-dblp.ungraph-75000.txt as-Caida.undir.txt bio-protein-undir.txt soc-hamsterster.undir.txt soc-Youtube-75000.undir.txt
DFILESP3 = cit-HepPh.txt cit-HepTh.txt p2p-Gnutella31.txt ca-AstroPh.txt email-EuAll.txt soc-Slashdot0811-75000.txt cit-Cora.txt soc-digg.txt soc-flickr-75000.txt soc-pokec-75000.txt soft-jdkdependency.txt text-spanishbook.txt

unittest:
	chmod a+rwx `pwd`
	for file in $(UNITTESTFILE); do \
		mkdir output_$$file && \
		python gm_kcore.py --file `pwd`/data/$$file --dest_dir `pwd`/output_$$file --unweighted >> stdout_$$file && \
		sort -k1 -n `pwd`/output_$$file/conncomp-kcore.csv >> `pwd`/output_$$file/conncomp-kcore-sorted.csv && \
		diff `pwd`/output_$$file/conncomp-kcore-sorted.csv `pwd`/data/ans_$$file; done
	@echo 'Unit test passed'

gm1:
	chmod a+rwx `pwd`
	for file in $(DFILESP1); do \
		mkdir output_$$file && \
		python gm_main_p1.py --file `pwd`/data/$$file --dest_dir `pwd`/output_$$file --unweighted >> stdout_$$file; done

gm2:
	chmod a+rwx `pwd`
	for file in $(UFILESP2); do \
		mkdir output_$$file && \
		python gm_main_p2.py --file `pwd`/data/$$file --dest_dir `pwd`/output_$$file --unweighted --undirected >> stdout_$$file; done
	for file in $(DFILESP2); do \
		mkdir output_$$file && \
		python gm_main_p2.py --file `pwd`/data/$$file --dest_dir `pwd`/output_$$file --unweighted >> stdout_$$file; done

gm3:
	chmod a+rwx `pwd`
	for file in $(UFILESP3); do \
		mkdir output_$$file && \
		python gm_main_p3.py --file `pwd`/data/$$file --dest_dir `pwd`/output_$$file --unweighted --undirected >> stdout_$$file; done
	for file in $(DFILESP3); do \
		mkdir output_$$file && \
		python gm_main_p3.py --file `pwd`/data/$$file --dest_dir `pwd`/output_$$file --unweighted >> stdout_$$file; done

install:
	sudo apt-get install python-psycopg2

all.tar:
	tar -zcvf graphminer.tar.gz *.txt makefile *.py matlab output doc

clean:
	rm *.pyc
