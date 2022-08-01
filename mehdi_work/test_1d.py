Experiment(description='Test with 1D data for playing',
           data_dir='./data/',
           max_depth=4, 
           random_order=False,
           k=1,
           debug=False, 
           local_computation=True, 
           n_rand=1,
           sd=2, 
           jitter_sd=0.1,
           max_jobs=300, 
           verbose=False,
           make_predictions=False,
           skip_complete=False,
           results_dir='./results/',
           iters=100,
           base_kernels='SE,Per,Lin,Const',
           random_seed=1,
           period_heuristic=5,
           period_heuristic_type='min',
           subset=True,
           subset_size=250,
           full_iters=10,
           bundle_size=5,
           additive_form=False,
           mean='ff.MeanZero()',      # Starting model
           kernel='ff.NoiseKernel()', # Starting kernel
           lik='ff.LikGauss(sf=-np.Inf)', # Starting likelihood 
           score='pl2',
           search_operators=[('A', ('+', 'A', 'B'), {'A': 'kernel', 'B': 'base'}),\
                             ('A', 'B', {'A': 'kernel', 'B': 'base'}),\
                             ('A', ('None',), {'A': 'kernel'}),\
                             ('A', ('CP', 'd', 'A'), {'A': 'kernel', 'd' : 'dimension'})])
