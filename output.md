**[[Cancer Nanotech]]
[[Proposal Requirements]]
[[Nanotech Research Proposal (archive)]]




# Title
 Combining microfluidic concentration gradient generators, tumour spheroid arrays and batch Bayesian optimisation to enable high-throughput combinatorial therapy screening
# Lay summary




# Scientific Summary

Combination therapies for cancer, rely on evolutionary guiding tumour cell populations to maximise the combined effect of chemotherapy drugs applied in series. Such approaches have been repeatedly shown to provide better patient outcomes via (increased efficacy and decreasing off-site toxicity) and are defined by higher than additive therapeutic index that would be expected from combining the effect of each individual drug. Despite their benefit, sequential combination therapies are underexplored compared to concurrent combination therapies (drugs applied simultaneously).

At its heart, the research proposal focusses on combining 2 rapidly advancing technologies: high-throughput tumour spheroids and efficient parameter exploration models into a lab-in-a-loop platform capable of exploiting the unrealised gains within the research gap and providing new avenues for personalized medicine.

Tumour spheroids are just a step bellow in-vivo representativeness of animal models, bellow organoid chips, but are relatively inexpensive to produce en masse. They have been successfully used for screening of combinatorial drugs and can be rapidly cultured, thus allowing quick iteration cycles.  

Modifications of Bayesian Optimisation (BO), a black box parameter exploration, would allow to maximise sample efficiency, thus decreasing experimentation cost and making such exploration feasible. Sequential screening (compared to simultaneous screening), provides a much larger parameter space to explore, where emerging drug dose delivery sequence,  duration, and timings invoke the curse of dimensionality and thus make conventional screening approaches unfeasible. More importantly, if combined with standardized platform, BO allows for integration of prior information, thus massively accelerating testing.

Lastly, due to standardised properties of the system and BO suitability to transfer learning, the platform could be easily adapted for precision medicine. The explored sequential therapy space provides a priori, which would allow to rapidly and adaptively reevaluate the most salient therapy combinations with patient cells.





## Timeliness and Novelty


Multi-phase treatment strategies, have been repeatedly shown to outperform the application of single drug for cancer treatment. The structured application of drugs allows to steer the tumour evolution thus promoting targeted vulnerabilities in the tumour cell population non affected by a prior drug in the series. This approach provides a solution to developed drug-resistance and high toxicity of combined-drug strategies. However, despite improved treatment outcomes, and rapidly mounting number of newly discovered drugs, development of new multi-phase campaigns remains sporadic and non-systematic.


Recent explosion in machine learning and high throughput screening has significantly accelerated cancer drug discovery rate. In-silico tools, such as docking simulations, structure-based supervised leaning, or protein folding, allow to identify salient targets for further wet-lab testing at a comparatively low cost. This computational screening is then often combined with automated screening of drug efficacy using various in vitro models (e.g. organoids or tumour spheroids on Microfluidic chips.
## Research Proposal (4 pages)
### Background

#### Tumour Spheroids 
Tumour spheroids (and organoids) are 3D culture models that bridge the gap between 2D cell lines and animal studies by providing genetically and histologically representative tumour architecture while preserving cellular heterogeneity \cite{guntiOrganoidSpheroidTumor2021}. They reproduce proliferative, quiescent and necrotic zones, making them strong candidates for in-vitro drug screening. Although early spheroid methods were labour-intensive, several automated platforms now enable high-throughput generation of uniform spheroids \cite{jeonAutomatedHighContentHighThroughput2025} \cite{kondoHighthroughputScreeningColorectal2019} \cite{mosaadMicrowellmeshHighthroughput3D2018} \cite{pongAutomatedUniformSpheroid2024}.


#### BO in cancer therapy
Bayesian optimization (BO) is a concrete algorithmic application of the Bayesian Decision Theory (BDT), which provide a formal framework for optimal decision making under uncertainty and with prior knowledge (a prior). BDT has been repeatedly proposed to be medical dose finding trials \cite{mullerBayesianDecisionTheoreticDoseFinding2006}, \cite{whiteheadBAYESIANDECISIONPROCEDURES1995}, \cite{abrahamRobustBayesianDecision2004}, \cite{donagherIndividualisedMedicineWhy2017}; but has been limited to Bayesian dosing dashboards for inflammatory bowel disease \cite{strikEfficacyDashboardDriven2021}, \cite{dubinskyDashboardDrivenAcceleratedInfliximab2022}, \cite{santacanajuncosaBayesbasedDosingInfliximab2021}.


BO, originally popularised for ML hyperparameter tuning, has now been adopted in empirical sciences, mainly in context chemistry and materials science \cite{wangBayesianOptimizationChemical2022,@jinBayesianOptimisationEfficient2023,@packwoodBayesianOptimizationMaterials2017,@haseGryffinAlgorithmBayesian2021}. Biomedical applications include in-vitro drug-lead screening \cite{pyzer-knappBayesianOptimizationAccelerated2018,@dangPreferentialMultiObjectiveBayesian2025}, protein-formulation optimisation \cite{huynhRapidIdentificationProtein2023}, and fitting complex biological models \cite{colopyBayesianOptimisationGaussian2017,@borowskaBayesianOptimisationEfficient2022}. Notably, Yakavets et al. (2025) applied BO to a three-drug sequential regime in breast-cancer spheroids but failed due to poorly encoded variables and an over-dimensional (7D) design relative to sample size (n = 40) \cite{yakavetsMachineLearningassistedExploration2025}.


#### Microfluidics

### Research aims and objectives
**Hypothesis. A 3-inlet concentration gradient generator microfluidic chip can be paired with physiological-flow replicating tumours spheroid arrays to enable high throughput screening of combinatorial therapies.

\textbf{Deliverables}
\textbf{Objective 1 (O1).} Design, simulate and fabricate a microfluidic chip that exposes hydrogel-embedded spheroid arrays to a reproducible 3-solution concentration gradient.

\textbf{Objective 2 (O2).} Demonstrate reliable NSCLC (A549) spheroid formation, viability and drug-response readouts on-chip, and show that known synergistic combinations can be replicated.

\textbf{Objective 3 (O3).} Develop and benchmark a structured-batch Bayesian optimisation (SBBO) workflow tailored to gradient-generated batches, first in-silico and then on the microfluidic platform.

\textbf{Objective 4 (O4, reach objective).} Apply SBBO to explore and identify previously untested candidate synergistic drug sequences for NSCLC, providing ranked combinations for future validation.

### Research plan (divided in milestones)

1. \textbf{Design and Build a 2D MGG chip platform for Tumour Spheroid screening (O1)}:  The chip will be developed using SolidWorks and COMSOL CFD, with fabrication via standard PDMS photo-lithography workflows available in the CRUK nanofabrication facility \cite{MicroNanofabrication}. These established tools allow rapid design–test iterations, ensuring feasibility within the project timescale.
	1. \textbf{Design a modified 3-solution mixer} Although PDMS chips can be fabricated reliably via photolithography and soft lithography, the primary throughput bottleneck remains the limited number of syringe pumps available for delivering distinct conditions
		1. \textbf{Expand and test the 3 solution mixer} Thus, we adapt the concentric ring Tai Chi spiral 3-inlet mixer from Shen et al, which generates 24 linear combinations from 3 injected solutions by \cite{shenConstructionMultipleConcentration2023}. \cite{shenConstructionMultipleConcentration2023}. Channel width and geometry will be adjusted to support flow of ~96 µm·s⁻¹ needed for the larger spheroid arrays rather than the original single-cell screening array design. The mixer is designed following  recursive pattern - generating $3*2^n$ unique concentrations for n. Thus, if CFD predicts stable flow, scaling beyond 24 outputs (e.g., to 48–96) will be attempted; otherwise the validated (R² = 0.9946) 24-output design from Shen et al. will be used \cite{shenConstructionMultipleConcentration2023,2. \textbf{Test mixing robustness}. Mixing performance and noise will be quantified by perfusing fluorescein through one inlet and water through the other two, followed by fluorescent imaging. If acceptable concentration noise levels are not achieved (concentration Signal to Noise (StN) ratio >5%), the number of mixer rings will be decreased. Since all inlets are supposed to inject fluid at identical rate, a design where single motor drives 3 syringes can be implemented.
	2. \textbf{Integrate a physiological flow Tumour spheroid array} Prince et al 2022 [@princeMicrofluidicArraysBreast2022} describes a well-scaling technique to generate Tumour Spheroid arrays under flow conditions.  
		1. \textbf{Confirm Tai-Chi spiral comparability with hydrogel injection}. This hydrogel-loading method already works in “Christmas tree” CGGs \cite{princeMicrofluidicArraysBreast2022}, so similar behaviour is expected in Tai-Chi mixers. We will test a configuration of 8 spiral stages feeding five 20-cavity arrays to confirm that EKGel precursor consistently fills the cavities, first in CFD and then experimentally. EKGel (1 wt.% a-CNCs and 2 wt.% gelatin) is employed due to its long gelation time of 50 minutes, which gives sufficient time to invade the cavities and can be purged from channels using fluorinated oil \cite{princeMicrofluidicArraysBreast2022}. Afterwards, the whole setup will be investigated by brightfield microscopy. Lack of hydrogel within tumour-designated cavities and presence within mixing system will be considered a failure.  If cavity filling is inconsistent or hydrogel cannot be purged from mixing system, a dedicated phase-guide or micro-post separated channels will be introduced.  These can later be sealed with adhesive tape or epoxy glue \cite{temizLabonachipDevicesHow2015}. 
	
		2. \textbf{Integrate 3-solution mixer with cavity arrays}. The cavity arrays (4 lines, 20 each) will then be integrated at the end of of the 3-solution mixer.  Upon successful hydrogel-cavity filling, the CGG capabilities (fluorescence inside cavities) will be reevaluated as in step [step Test Mixing Robustness]. If successful, hydrogel  and fluorinated oil injection through single inlet (remaining inlets plugged) will be investigated. 

2. \textbf{Benchmark drug-dose response generation (O2)}  We next benchmark the device’s ability to produce reproducible drug–response data. Quantifying variance in delivered concentrations and spheroid viability is essential for subsequent BO modelling.
	1. \textbf{Spheroid Generation}. The seeding approach from Prince et al is adapted (cancer cells premixed with EKG precursor \cite{princeMicrofluidicArraysBreast2022}) using the A549 cell line derived from a human lung adenocarcinoma, a non-small cell lung cancer (NSCLC). The A549 can be acquired from the ECACC COSMIC cell lines, available through the UK Health and Security Agency \cite{COSMICCellLines}.  A549 spheroids reliably form in matrices similar to EkGEL (e.g. Matrigel or polyPEGDA–gelatin) \cite{dongSituTailoredConfining2025}. EKGel has similar properties and is used due to slow-gelling time required for cavity filling procedure \cite{princeMicrofluidicArraysBreast2022}, \cite{tarassoliCandidateBioinks3D2018}. Prior to hydrogel mixing, the cells will be incubated with 20 µM of Cell Explorer Live Cell Tracking dye (or alternative) and resuspended in media, to allow Two-photon Confocal Laser Microscopy Scanning (TP-CLSM) \cite{jeonAutomatedHighContentHighThroughput2025}. Spheroids will mature over 6 days under continuous perfusion, following established protocols \cite{dongSituTailoredConfining2025}.
	2. \textbf{Linear-concentration benchmarking}. Gradient performance will be validated using cisplatin, which produces consistent spheroid toxicity profiles \cite{barrera-rodriguezMultidrugResistanceCharacterization2015}. Three inlet concentrations (0, 5, 10 µM) spanning the active range \cite{gansukhVitroAnalysisRelationships2013} yield ≥24 discrete conditions. This provides a feasible, low-cost cell-viability benchmark for noise levels and later multi-drug tests. 
	3.  \textbf{Integration of Automated imaging analysis} Jeon et al 2025 TP-CLSM analysis pipeline will be adapted to spheroid arrays, which have lower spatial complexity than inverted colloidal crystals, minimising development time.\cite{jeonAutomatedHighContentHighThroughput2025}

	4. \textbf{3 Drug benchmarking}. Three-drug benchmarking will use the same protocol as the cisplatin gradient, but with fixed inlet concentrations for two additional agents: necitumumab and gemcitabine. This restricts experimental scope to synergistically confirmed 3-drug combination therapy \cite{watanabeNecitumumabGemcitabineCisplatin2019}, while  a manageable subset  while demonstrating compatibility with multi-drug designs. Moreover, the cell viability measurements from a single chip are sufficient for estimation of effect-based drug synergy metrics (e.g. bliss-independence) \cite{duarteEvaluationSynergismDrug2022}. Moreover, the chips suitability to generate linear concentration gradients, readily allows to adapt it to more robust dose-effect models \cite{duarteEvaluationSynergismDrug2022}, \cite{zhaoNewBlissIndependence2014}. 
	5. \textbf{Publication} Regardless of BO integration, a validated novel spheroid–gradient platform is a publishable outcome (e.g., _Nano Letters_, _Advanced Healthcare Materials_, _Microsystems & Nanoengineering_, _Lab on a Chip_). This ensures intermediate deliverables even if later milestones prove challenging.
	
3. \textbf{Design and in-silico test a experimental design tailored Bayesian Optimisation (O3)}. Standard batch BO assumes free target selection, whereas CGGs yield structured concentration sets. Since physical and labour microfluidic screening constraints are harder to solve,  active-learning policy must thus be adapted to work under these constrains. 

	1. \textbf{Implement Structured-Batch Bayesian Optimisation (SBBO) algorithm}. As shown in [figure], the three inlet concentrations allow exploring the parameter space along discrete points on edges of arbitrary triangles.  

		1. \textbf{In-silico testing setup} Note that *This work is purely computational and will run during experimental downtime*. BO will be implemented in Python using BoTorch/PyTorch libraries \cite{balandatBoTorchFrameworkEfficient2020}, \cite{paszkePyTorchImperativeStyle2019}. All algorithms will be benchmarked using Ackley, Rosenbrock, and Hartmann functions within  relevant dimensionality space \cite{OptimizationTestFunctions}. Evaluation metrics will be: 90% convergence speed, simple and cumulative regret \cite{garnettBayesianOptimization2023}. 
		2. \textbf{Implement a linear-space acquisition function}. An acquisition function defines the salience of any data point being investigated. We will adapt the acquisition function to score lines of _n_ discrete points between two inlets by cumulative (all points on the line) utility, and validate converge to optimum on 3D test functions.
	
		3. \textbf{Implement a structured batch acquisition function} We then extend the paradigm  to structured triangular batches defined by three inlet concentrations [figure X]. If the triangle search space becomes too large, we will use a secondary optimisation routine to propose candidate triangles.
	2. \textbf{Benchmark and computationally optimize SBBO}
		1. \textbf{Low-dimension benchmarking}
		2. SBBO will be benchmarked against batch-BO, evolutionary methods, binary search, random, and grid search in 4D. Each algorithm evaluates up to 216 points across 100 seeds. SBBO should underperform batch-BO but exceed baseline methods. The simulations will be ran in parallel on Imperial's HPC systems.
		3. \textbf{Algorithm optimization (reach objective)} The unoptimized algorithm will likely be computationally expensive in high dimensions, thus making less myopic approaches unfeasible. Standard BO optimisation tricks will be implemented and any remaining downtime spent on solution search \cite{garnettBayesianOptimization2023}. Given the days-long duration of empirical microfluidic batch, hours-long runtime is acceptable. 
		4. \textbf{High-Dimensional Benchmarking (reach objective)} SBBO will be tested in 6D using 7D benchmarks, mimicking six-drug synergy searches. It should outperform all baselines except BO variants. If  BO is unexpectedly outperformed by an alternative algorithm capable of structured batch generation, it will be abandoned in favour of the algorithm.
	3. \textbf{Adapt SBBO for biological noise} Once empirical platforms noise estimates are available, SBBO will be adapted for heteroscedastic settings.
		1. \textbf{Adapt objective function to noise}. Objective functions model the underlying distribution constructed from investigated points and are used when generating new targets \cite{garnettBayesianOptimization2023}. To avoid noise-driven overfitting, empirical noise levels will be incorporated into the objective by use of Matern kernel, homoscedastic or heteroscedastic gaussian process, or more suitable alternative.
		2. \textbf{Benchmark  SBBO in noisy environment} The algorithm capability to discover optimums will be reevaluated in noisy settings. The exploration efficiency is likely to drop; inability to rediscover an optimum or optimum-proximate region will be considered an objective failure of the algorithm. However, this needs empirical estimation of platforms noise levels.
4. \textbf{Run empirical SSBO trial (O4)} A proof-of-concept SSBO-guided campaign will be run in a four-drug space. Exploration of five to six drugs will be treated as a reach objective, pursued only if earlier milestones complete ahead of schedule. At the appropriate stage, the system will be used to identify promising drug candidates in accordance with future research trends.
	1. \textbf{Establish single-drug dose–response curves.} Single-drug gradients (one chip per drug, run in parallel) will be used to fit simple dose–response models. These will define the initial prior and objective for SSBO, reusing the linear-gradient protocol from O2 to keep the experimental workload manageable.
	2. \textbf{Lab-in-a-loop workflow.} SSBO will be run for \textbf{up to 10 batches} (two chips per batch), which is sufficient to demonstrate closed-loop operation without exceeding realistic chip and culture throughput. For each batch, SSBO proposes three inlet drug cocktails per chip; after imaging, spheroid viability metrics are extracted and fed back into SSBO to generate the next batch.
	3. \textbf{Results.} We will evaluate SSBO identified optimums against control and known combinatorial studies. Evidence that SSBO achieves better viability outcomes or finds promising regions faster will demonstrate practical value, even without fully mapping the search space, and would constitute a publishable case study.


### Pathway to Impact



High-throughput exploration of multi-drug dose–response relationships in physiologically relevant models is currently limited by both hardware and experimental-design constraints. Most microfluidic chips can only generate linear concentration gradients and have poor microfluidic pump to screened conditions ratio. Typical workflows are equipment and manual labour intense and require performing multiple experiments just to investigate synergies in dose-response grid of just two drugs.


By explicitly coupling a three-inlet gradient generator, tumour spheroid arrays and a structured-batch Bayesian optimisation algorithm, this project will deliver a proof-of-concept platform for data-driven exploration of multi-drug therapies. In the short term, this can reduce the experimental burden of identifying promising drug sequences for NSCLC, and provide a reusable methodology for other cancer types and drug classes. The platform is designed around widely used materials (PDMS, gelatin-based hydrogels) and open-source analysis pipelines, facilitating replicability and transfer learning.


In the longer term, the main impact lies in precision oncology. Once a baseline SBBO model has been trained on generic cell lines, the same framework could be adapted to patient-derived cells, using transfer learning to rapidly refine treatment sequences under the constraints of limited sample material and time. This aligns with current clinical interest in functional precision medicine and could provide a principled experimental-design layer above existing ex-vivo drug screening assays. Beyond cancer, the structured-batch optimisation concept is broadly applicable to any microfluidic gradient platform in drug delivery, toxicology or tissue engineering.


# \textbf{Gantt Chart} (3 years)
