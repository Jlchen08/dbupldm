Manuscript Number: BDR-D-25-00303R3 

Dual Balanced Large Marginal Machine for Imbalanced Data Classification 

Dear Prof Huang,  

Thank you for submitting your manuscript to Big Data Research. 

I have completed my evaluation of your manuscript. The reviewers recommend reconsideration of your manuscript following minor revision and modification. I invite you to resubmit your manuscript after addressing the comments below. Please resubmit your revised manuscript by 07/05/2026. 

When revising your manuscript, please consider all issues mentioned in the reviewers' comments carefully: please outline every change made in response to their comments and provide suitable rebuttals for any comments not addressed. Please note that your revised submission may need to be re-reviewed.  

To submit your revised manuscript, please log in as an author at https://www.editorialmanager.com/bdr/, and navigate to the "Submissions Needing Revision" folder under the Author Main Menu.  
Research Elements (optional)
This journal encourages you to share research objects - including your raw data, methods, protocols, software, hardware and more – which support your original research article in a Research Elements journal. Research Elements are open access, multidisciplinary, peer-reviewed journals which make the objects associated with your research more discoverable, trustworthy and promote replicability and reproducibility. As open access journals, there may be an Article Publishing Charge if your paper is accepted for publication. Find out more about the Research Elements journals at https://www.elsevier.com/authors/tools-and-resources/research-elements-journals?dgcid=ec_em_research_elements_email.


Big Data Research values your contribution and I look forward to receiving your revised manuscript.￼ 

Kind regards,  

Longbiao Chen 

Editor-in-Chief 

Big Data Research 

Editor and Reviewer comments:  



Reviewer #7: The manuscript has undergone three rounds of revision and is now highly polished. The authors have addressed the reviewers' concerns regarding:
- Comparison with the latest state-of-the-art models.Scalability for Big Data paradigms.Experimental reproducibility.
- Terminology consistency.The paper provides a meaningful incremental advance in margin distribution learning. While the $O(n^3)$ complexity is a hurdle for "Big Data," the provided theoretical paths toward distributed and approximated versions justify its publication.
- Final Suggestion to Authors:Before final publication, ensure that the "Supplementary Material" links are finalized and that all magenta/orange highlighting from the revision process is removed for the final production version.


Reviewer #8: The authors have moved the manuscript forward in this round. The new Remark 2 clarifying "quantile distance" versus "composite distance" is useful, the MLP+Focal configuration is now properly specified, and the limitations discussion in the conclusion is a real improvement. That said, the new head-to-head against DeepSMOTE, LDAM, and Balanced Softmax introduces problems that need to be resolved, and several issues that should have been caught in earlier rounds are still present. I recommend major revision.

Strengths
-----------

1) The new Remark 2 clearly distinguishes the two distance concepts that were previously conflated. This was a real source of confusion in R2 and the fix is well done.

2) The expanded MLP+Focal configuration in Section 5.3 (architecture, optimizer, β values, batch size, LR schedule, grid search ranges) is detailed enough for reproducibility.

3) The limitations paragraph in the conclusion (training complexity, extreme imbalance, concept drift, unstructured data) gives a more balanced positioning of the method than earlier versions.

4) The scalability discussion (ADMM, mini-batch, Random Fourier Features) at least acknowledges the journal's scope, even if it is not yet demonstrated.

Major Concerns
------------------

1) The LDAM configuration as described is methodologically incoherent. The authors write that LDAM "adapts ResNet-18 for tabular data." ResNet-18 is a 2D convolutional architecture designed for image inputs. There is no standard way to apply it to tabular features of dimension 3 to 61, which is the range in Table 1. The authors need to explain exactly what architecture was used, replace it with a sensible tabular backbone (MLP with LDAM loss would be the natural choice), or drop the claim. As it stands, readers cannot reproduce or evaluate this baseline.

2) Please release the code, seeds, and fold-level outputs for Table 7. The ordering LDAM > Balanced Softmax > DeepSMOTE is very consistent across the 17 datasets and across Accuracy, AUC, and F1. This ordering is plausible on its own, but the consistency is unusual enough that the paper should provide a reproducibility package (code, random seeds, per-fold numbers). This would also address Reviewer 5's original reproducibility request in a more complete way.

3) The Wilcoxon p-value reporting needs more detail. Reporting p = 0.03125 for all four comparisons (DBUPLDM vs SVM, UPSVM, PinSVM, LDM) is consistent with a test over 5 or 6 paired observations where DBUPLDM wins all of them, but the paper does not say what the paired units are (datasets? η values? η × datasets?) or what n is. Please state the test setup and report effect sizes alongside the p-values. A one-line description would clear this up.

4) Text-table inconsistency. Section 5.3 says "deep learning methods show strong performance on certain datasets (e.g., LDAM on Ionosphere and Australia)." In Table 7, DBUPLDM beats LDAM on Australian (87.24 vs 84.20). Pick examples that actually match the table, or remove the specific claim.

5) Big Data Research scope is still only rhetorical. The new scalability paragraph in the conclusion discusses ADMM, mini-batch processing, and Random Fourier Features, but none of this is implemented or evaluated. The experiments are entirely on small UCI datasets (hundreds to about a thousand samples). At minimum, I would ask for one empirical demonstration on a larger-scale imbalanced dataset (for example, CreditCard Fraud with ~285k samples, KDD99, or a similar public benchmark) to support the scalability claims. Without this, the journal fit remains weak.

6) Novelty over the authors' own prior work should be spelled out. The UP loss applied to a large-margin distribution classifier already appears in Gu et al. 2024 (cited in the paper). The dual balance factor is close in spirit to Cheng et al.'s CS-LDM (2016). The paper's contribution is essentially the combination of these two ingredients. A short paragraph in the introduction or Section 3 stating what is new here relative to Gu et al. 2024 would strengthen the case.

Minor Issues
--------------

1) Title: "Dual Balanced Large Marginal Machine" should be "Large Margin Machine" (or "Large Margin Distribution Machine" to match the abstract). This has remained wrong across rounds and needs to be fixed.

2) Dataset naming is inconsistent. Table 1 lists "Herberman," the results tables use "Heberman," and Table 7 uses "Habe." The dataset is Haberman's Survival. Pick one spelling and use it throughout.

3) "Ecoil" should be "Ecoli" (E. coli dataset).

4) "Germans" should likely be "German" (German Credit dataset).

5) "Phonemes" vs "Phoneme" is inconsistent between Table 1 and Section 5.5.

6) Table 7, WDBC row: "87.50/91.43/0/89" has a slash where a decimal should be. Should read "0.89."

7) Figure 6, subfigures (i), (j), (k), and (l) are all captioned "Prlx dataset." These are clearly different datasets. Fix the captions.

8) Figure 6(g) caption reads "Daibetes dataset." Should be "Diabetes."

9) Section 5.5: "PinSVM, UPSVM, and DBUPLDM) performe well" should be "perform."

10) The Section 1 roadmap reads "Section 3 proposes the Dual Balanced method and DBUPLDM model. Section 5 discusses…" Section 4 (Properties of DBUPLDM) is skipped. Add it.

11) Table 5 caption "Minimum distance with second order statistics" does not describe the content (ablation over balanced factors and hinge vs UP loss). Rewrite.

12) Remark renumbering: the new Remark 2 (Terminology Clarification) shifts former Remark 2 to Remark 3 and former Remark 3 to Remark 4. Please verify no downstream cross-references still point to the old numbers.

13) The third contribution bullet in the introduction says "the quantile distance is introduced to replace the shortest distance between sample sets in traditional LDM." Given the new Remark 2, this is imprecise (the replacement involves both the UP loss and the composite distance). Reword for consistency.

14) The response letter header says "BDR-D-25-00303R3" but the opening paragraph says "R1," and later describes this as the third round. Fix this.

15) Reviewer 6's comment about "deeper theoretical insight" is acknowledged in the response but not concretely addressed. A brief sentence on what was done, or why no change was needed, would help.
  

More information and support 

FAQ: How do I revise my submission in Editorial Manager?

https://service.elsevier.com/app/answers/detail/a_id/28463/supporthub/publishing/

FAQ: How can I reset a forgotten password?
https://service.elsevier.com/app/answers/detail/a_id/28452/supporthub/publishing/
For further assistance, please visit our customer service site: https://service.elsevier.com/app/home/supporthub/publishing/
Here you can search for solutions on a range of topics, find answers to frequently asked questions, and learn more about Editorial Manager via interactive tutorials. You can also talk 24/7 to our customer support team by phone and 24/7 by live chat and email

At Elsevier, we want to help all our authors to stay safe when publishing. Please be aware of fraudulent messages requesting money in return for the publication of your paper. If you are publishing open access with Elsevier, bear in mind that we will never request payment before the paper has been accepted. We have prepared some guidelines (https://www.elsevier.com/connect/authors-update/seven-top-tips-on-stopping-apc-scams ) that you may find helpful, including a short video on Identifying fake acceptance letters (https://www.youtube.com/watch?v=o5l8thD9XtE ). Please remember that you can contact Elsevier s Researcher Support team (https://service.elsevier.com/app/home/supporthub/publishing/) at any time if you have questions about your manuscript, and you can log into Editorial Manager to check the status of your manuscript (https://service.elsevier.com/app/answers/detail/a_id/29155/c/10530/supporthub/publishing/kw/status/).

#AU_BDR#

To ensure this email reaches the intended recipient, please do not delete the above code