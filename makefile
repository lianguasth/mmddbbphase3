all:
	unittest plot report

unittest:
	@echo 'Running unit test'
	mkdir output-unittest
	cd graphminer; make unittest; mv output_* ../output-unittest; mv stdout_* ../output-unittest

plot:
	mkdir pic; mkdir res
	#mkdir output-phase1
	#cd graphminer; make gm1; mv output_* ../output-phase1; mv stdout_* ../output-phase1
	python iterateOverDir.py output-phase1/ 1
	#mkdir output-phase2
	#cd graphminer; make gm2; mv output_* ../output-phase2; mv stdout_* ../output-phase2
	python iterateOverDir.py output-phase2/ 2
	#mkdir output-phase3
	#cd graphminer; make gm3; mv output_* ../output-phase3; mv stdout_* ../output-phase3
	./plot.sh output-phase3

report:
	mv pic/* report/FIG
	cd report; make; cp paper.pdf ../report.pdf
	@echo 'Report generated'

clean:
	rm -r output*
	rmdir pic
	cd report; make spotless
	cd report/FIG; rm *;
	cd graphminer; make clean
