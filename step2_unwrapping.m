%function [ph_uw,msd]=uw_3d(ph,xy,day,ifgday_ix,bperp,options)

bperp = readmatrix('bperp.txt');
day = readmatrix('day.txt');
ifgday_ix = readmatrix('ifgday_ix.txt');
ph = readmatrix('ph.txt');
xy = readmatrix('xy.txt');

%%%%%%%%%%%%  set options %%%%%%%%%%%%%%%%
%%%% you may need to edit below to customize %%%
options=struct;
options.time_win=getparm('unwrap_time_win',1)
options.unwrap_method=getparm('unwrap_method',1)
options.grid_size=getparm('unwrap_grid_size',1)
options.prefilt_win=getparm('unwrap_gold_n_win',1)
options.goldfilt_flag=getparm('unwrap_prefilter_flag',1)
options.gold_alpha=getparm('unwrap_gold_alpha',1)
options.la_flag=getparm('unwrap_la_error_flag',1)
options.scf_flag=getparm('unwrap_spatial_cost_func_flag',1)

%n_trial_wraps
max_topo_err = 50.;
lambda=0.0555;  % radar wavelength in meter
rho = 830000; % mean range - need only be approximately correct
inc_mean=21*pi/180; % incidence angle
max_K=max_topo_err/(lambda*rho*sin(inc_mean)/4/pi);
bperp_range=max(bperp)-min(bperp);
options.n_trial_wraps=(bperp_range*max_K/(2*pi))
%%% you may need to edit above to customize %%%
 
[ph_uw,msd] = uw_3d(ph,xy,day,ifgday_ix,bperp, options); % 

% save ph_uw to ascii file
writematrix(ph_uw,'ph_uw.txt','Delimiter','tab');



