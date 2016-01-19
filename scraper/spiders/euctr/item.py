# -*- coding: utf-8 -*-
# pylama:skip=1
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import scrapy


class Item(scrapy.Item):

    # Plain value fields

    member_state_concerned = scrapy.Field()
    eudract_number = scrapy.Field()
    full_title_of_the_trial = scrapy.Field()
    # title_of_the_trial_for_lay_people_in_easily_understood_i_e_non_technical_language = scrapy.Field()
    sponsor_s_protocol_code_number = scrapy.Field()
    trial_is_part_of_a_paediatric_investigation_plan = scrapy.Field()
    name_of_sponsor = scrapy.Field()
    country = scrapy.Field()
    status_of_the_sponsor = scrapy.Field()
    name_of_organisation_providing_support = scrapy.Field()
    country = scrapy.Field()
    name_of_organisation = scrapy.Field()
    functional_name_of_contact_point = scrapy.Field()
    street_address = scrapy.Field()
    town_city = scrapy.Field()
    post_code = scrapy.Field()
    country = scrapy.Field()
    telephone_number = scrapy.Field()
    imp_role = scrapy.Field()
    # imp_to_be_used_in_the_trial_has_a_marketing_authorisation = scrapy.Field()
    # trade_name = scrapy.Field()
    # name_of_the_marketing_authorisation_holder = scrapy.Field()
    # country_which_granted_the_marketing_authorisation = scrapy.Field()
    # the_imp_has_been_designated_in_this_indication_as_an_orphan_drug_in_the_community = scrapy.Field()
    # pharmaceutical_form = scrapy.Field()
    # specific_paediatric_formulation = scrapy.Field()
    # routes_of_administration_for_this_imp = scrapy.Field()
    # inn_proposed_inn = scrapy.Field()
    # cas_number = scrapy.Field()
    # other_descriptive_name = scrapy.Field()
    # ev_substance_code = scrapy.Field()
    # concentration_unit = scrapy.Field()
    # concentration_type = scrapy.Field()
    # concentration_number = scrapy.Field()
    # active_substance_of_chemical_origin = scrapy.Field()
    # active_substance_of_biological_biotechnological_origin_other_than_advanced_therapy_imp_atimp_ = scrapy.Field()
    # advanced_therapy_imp_atimp_ = scrapy.Field()
    # somatic_cell_therapy_medicinal_product = scrapy.Field()
    # gene_therapy_medical_product = scrapy.Field()
    # tissue_engineered_product = scrapy.Field()
    # combination_atimp_i_e_one_involving_a_medical_device_ = scrapy.Field()
    # committee_on_advanced_therapies_cat_has_issued_a_classification_for_this_product = scrapy.Field()
    # combination_product_that_includes_a_device_but_does_not_involve_an_advanced_therapy = scrapy.Field()
    # radiopharmaceutical_medicinal_product = scrapy.Field()
    # immunological_medicinal_product_such_as_vaccine_allergen_immune_serum_ = scrapy.Field()
    # plasma_derived_medicinal_product = scrapy.Field()
    # extractive_medicinal_product = scrapy.Field()
    # recombinant_medicinal_product = scrapy.Field()
    # medicinal_product_containing_genetically_modified_organisms = scrapy.Field()
    # herbal_medicinal_product = scrapy.Field()
    # homeopathic_medicinal_product = scrapy.Field()
    # another_type_of_medicinal_product = scrapy.Field()
    # is_a_placebo_used_in_this_trial_ = scrapy.Field()
    # pharmaceutical_form_of_the_placebo = scrapy.Field()
    # route_of_administration_of_the_placebo = scrapy.Field()
    # medical_condition_s_being_investigated = scrapy.Field()
    # medical_condition_in_easily_understood_language = scrapy.Field()
    # therapeutic_area = scrapy.Field()
    # version = scrapy.Field()
    # level = scrapy.Field()
    # classification_code = scrapy.Field()
    # term = scrapy.Field()
    # system_organ_class = scrapy.Field()
    # condition_being_studied_is_a_rare_disease = scrapy.Field()
    # main_objective_of_the_trial = scrapy.Field()
    # secondary_objectives_of_the_trial = scrapy.Field()
    # trial_contains_a_sub_study = scrapy.Field()
    # principal_inclusion_criteria = scrapy.Field()
    # principal_exclusion_criteria = scrapy.Field()
    # primary_end_point_s_ = scrapy.Field()
    # timepoint_s_of_evaluation_of_this_end_point = scrapy.Field()
    # secondary_end_point_s_ = scrapy.Field()
    # timepoint_s_of_evaluation_of_this_end_point = scrapy.Field()
    # diagnosis = scrapy.Field()
    # prophylaxis = scrapy.Field()
    # therapy = scrapy.Field()
    # safety = scrapy.Field()
    # efficacy = scrapy.Field()
    # pharmacokinetic = scrapy.Field()
    # pharmacodynamic = scrapy.Field()
    # bioequivalence = scrapy.Field()
    # dose_response = scrapy.Field()
    # pharmacogenetic = scrapy.Field()
    # pharmacogenomic = scrapy.Field()
    # pharmacoeconomic = scrapy.Field()
    # others = scrapy.Field()
    # human_pharmacology_phase_i_ = scrapy.Field()
    # first_administration_to_humans = scrapy.Field()
    # bioequivalence_study = scrapy.Field()
    # other = scrapy.Field()
    # therapeutic_exploratory_phase_ii_ = scrapy.Field()
    # therapeutic_confirmatory_phase_iii_ = scrapy.Field()
    # therapeutic_use_phase_iv_ = scrapy.Field()
    # controlled = scrapy.Field()
    # randomised = scrapy.Field()
    # open = scrapy.Field()
    # single_blind = scrapy.Field()
    # double_blind = scrapy.Field()
    # parallel_group = scrapy.Field()
    # cross_over = scrapy.Field()
    # other = scrapy.Field()
    # other_medicinal_product_s_ = scrapy.Field()
    # placebo = scrapy.Field()
    # other = scrapy.Field()
    # number_of_treatment_arms_in_the_trial = scrapy.Field()
    # the_trial_involves_single_site_in_the_member_state_concerned = scrapy.Field()
    # the_trial_involves_multiple_sites_in_the_member_state_concerned = scrapy.Field()
    # the_trial_involves_multiple_member_states = scrapy.Field()
    # trial_being_conducted_both_within_and_outside_the_eea = scrapy.Field()
    # trial_being_conducted_completely_outside_of_the_eea = scrapy.Field()
    # trial_has_a_data_monitoring_committee = scrapy.Field()
    # definition_of_the_end_of_the_trial_and_justification_where_it_is_not_the_last_visit_of_the_last_subject_undergoing_the_trial = scrapy.Field()
    # in_the_member_state_concerned_years = scrapy.Field()
    # trial_has_subjects_under_18 = scrapy.Field()
    # in_utero = scrapy.Field()
    # preterm_newborn_infants_up_to_gestational_age_37_weeks_ = scrapy.Field()
    # newborns_0_27_days_ = scrapy.Field()
    # infants_and_toddlers_28_days_23_months_ = scrapy.Field()
    # children_2_11years_ = scrapy.Field()
    # adolescents_12_17_years_ = scrapy.Field()
    # adults_18_64_years_ = scrapy.Field()
    # number_of_subjects_for_this_age_range_ = scrapy.Field()
    # elderly_65_years_ = scrapy.Field()
    # number_of_subjects_for_this_age_range_ = scrapy.Field()
    # female = scrapy.Field()
    # male = scrapy.Field()
    # healthy_volunteers = scrapy.Field()
    # patients = scrapy.Field()
    # specific_vulnerable_populations = scrapy.Field()
    # women_of_childbearing_potential_not_using_contraception = scrapy.Field()
    # women_of_child_bearing_potential_using_contraception = scrapy.Field()
    # pregnant_women = scrapy.Field()
    # nursing_women = scrapy.Field()
    # emergency_situation = scrapy.Field()
    # subjects_incapable_of_giving_consent_personally = scrapy.Field()
    # others = scrapy.Field()
    # in_the_member_state = scrapy.Field()
    # plans_for_treatment_or_care_after_the_subject_has_ended_the_participation_in_the_trial_if_it_is_different_from_the_expected_normal_treatment_of_that_condition_ = scrapy.Field()
    # competent_authority_decision = scrapy.Field()
    # date_of_competent_authority_decision = scrapy.Field()
    # ethics_committee_opinion_of_the_trial_application = scrapy.Field()
    # ethics_committee_opinion_reason_s_for_unfavourable_opinion = scrapy.Field()
    # date_of_ethics_committee_opinion = scrapy.Field()
    # end_of_trial_status = scrapy.Field()

    # Helpers

    def add_data(self, key, value):
        if key in self.fields:
            self[key] = value
