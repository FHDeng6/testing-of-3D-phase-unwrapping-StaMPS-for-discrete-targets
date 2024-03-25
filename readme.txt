An algorithm to test the reliability of the 3D phase unwrapping method built in StaMPS using synthetic data. Note that the codes were designed for linear (temporally) velocity field. You may modified the code accordingly for non-linear cases. 

This code comes along with the paper: Fanghui Deng and Mark Zumberge. Seafloor motion from offshore platforms using satellite radar images – a case study in the Adriatic Sea. Under revision. 

The code was written and tested in Python 3.10.12 under Ubuntu 22.04. Steps of how to use the codes are as follows. 

1. Prepare the following files manually or use your own codes: xy.txt, day.txt, ifgday_ix.txt, bperp.txt, vel_real.txt. Examples files were given. 

	xy.txt: N x 3 matrix of coordinates (in metres) of PS points. N is the total number of PS points. The first column is not very necessary but is included to keep consistent with the format used in StaMPS. In our case, the second column is easting and the third column is northing. 

	day.txt: (M+1) x 1 vector giving image acquisition dates in days, relative to the reference image, i.e., the acquisition date of the reference image is 0. M is the total number of interferograms. 

	ifgday_ix.txt: M x 2 matrix giving index to dates of reference and secondary images in days for each interferogram. M is the total number of interferograms. 

	bperp.txt: perpendicular baselines,  M x 1 vector giving perpendicular baselines. 

	vel_real.txt: N x 1 vector giving displacement rate (in InSAR LOS direction) of each PS point, unit: mm/year. N is the total number of PS points.

2. Generate time sereis of wrapped phase by running script step1_create_wrapped_phase_ph.py. 

3. Open matlab and run script step2_unwrapping.m. You must have StaMPS installed before running this script.

4. Convert the unwrapped phase to displacement time sereis by running script step3_convert_unwrapped_phase_to_displacement.py

5. Calculate the linear rate of the above displacement time series by running script step4_calculate_observed_rate.py

6. Calculate the rate residual and visilize the results by running script step5_compare_plot_real_observed_velocity.py


For questions and feedbacks, please contact Fanghui Deng at fdeng4@central.uh.edu.

This is research code provided to you "AS IS" with no warranties of correctness. Use at your own risk.
