''' Unit tests for the base Korean CAS dictionary '''

import pytest
from plover_korean.cas.dictionaries.ko_cas_base import (
    lookup,
    OPERATOR_ATTACH
)


class TestLookup(object):
    ''' Test the base cases of lookup '''

    def test_length_zero(self):
        strokes = ()
        with pytest.raises(KeyError):
            lookup(strokes)

    def test_length_one(self):
        strokes = ('ㄴㅣㄱ',)
        test = lookup(strokes)
        assert test == f'닉{OPERATOR_ATTACH}'

    def test_length_two(self):
        strokes = ('ㄴㅣㄱ', 'ㄴㅣㄱ')
        with pytest.raises(KeyError):
            lookup(strokes)

    def test_english(self):
        strokes = ('HR',)
        with pytest.raises(KeyError):
            lookup(strokes)

    def test_steno_order_wrong(self):
        strokes = ('ㅈㅎ',)
        with pytest.raises(KeyError):
            lookup(strokes)

class TestLookupSyllableBlocks(object):
    ''' Test syllable block construction cases of lookup '''

    def test_initial_h_medial_o(self):
        strokes = ('ㅎㅗ',)
        test = lookup(strokes)
        assert test == f'호{OPERATOR_ATTACH}'

    def test_initial_m_medial_a(self):
        strokes = ('ㅁㅏ',)
        test = lookup(strokes)
        assert test == f'마{OPERATOR_ATTACH}'

    def test_initial_g_medial_u(self):
        strokes = ('ㄱㅜ',)
        test = lookup(strokes)
        assert test == f'구{OPERATOR_ATTACH}'

    def test_initial_j_medial_eo(self):
        strokes = ('ㅈㅓ',)
        test = lookup(strokes)
        assert test == f'저{OPERATOR_ATTACH}'

    def test_initial_n_medial_i(self):
        strokes = ('ㄴㅣ',)
        test = lookup(strokes)
        assert test == f'니{OPERATOR_ATTACH}'

    def test_initial_d_medial_eu(self):
        strokes = ('ㄷㅏㅓ',)
        test = lookup(strokes)
        assert test == f'드{OPERATOR_ATTACH}'

    def test_inintial_s_medial_ae(self):
        strokes = ('ㅅㅏㅣ',)
        test = lookup(strokes)
        assert test == f'새{OPERATOR_ATTACH}'

    def test_initial_b_medial_e(self):
        strokes = ('ㅂㅓㅣ',)
        test = lookup(strokes)
        assert test == f'베{OPERATOR_ATTACH}'

    def test_initial_r_medial_yo(self):
        strokes = ('ㄹㅗ*',)
        test = lookup(strokes)
        assert test == f'료{OPERATOR_ATTACH}'

    def test_initial_k_medial_ya(self):
        strokes = ('ㅎㄱㅏ*',)
        test = lookup(strokes)
        assert test == f'캬{OPERATOR_ATTACH}'

    def test_initial_ch_medial_yu(self):
        strokes = ('ㅎㅈㅜ*',)
        test = lookup(strokes)
        assert test == f'츄{OPERATOR_ATTACH}'

    def test_initial_t_medial_yeo(self):
        strokes = ('ㅎㄷ*ㅓ',)
        test = lookup(strokes)
        assert test == f'텨{OPERATOR_ATTACH}'

    def test_initial_t_medial_yae(self):
        strokes = ('ㅎㄷㅏ*ㅓ',)
        test = lookup(strokes)
        assert test == f'턔{OPERATOR_ATTACH}'

    def test_initial_p_medial_ye(self):
        strokes = ('ㅎㅂㅗㅓㅣ',)
        test = lookup(strokes)
        assert test == f'폐{OPERATOR_ATTACH}'

    def test_intitial_kk_medial_ui(self):
        strokes = ('ㄱㅇㅏㅓㅣ',)
        test = lookup(strokes)
        assert test == f'끠{OPERATOR_ATTACH}'

    def test_initial_jj_medial_oe(self):
        strokes = ('ㅈㅇㅗㅣ',)
        test = lookup(strokes)
        assert test == f'쬐{OPERATOR_ATTACH}'

    def test_initial_tt_medial_wi(self):
        strokes = ('ㄷㅇㅜㅣ',)
        test = lookup(strokes)
        assert test == f'뛰{OPERATOR_ATTACH}'

    def test_initial_ss_medial_wa(self):
        strokes = ('ㅇㅅㅗㅏ',)
        test = lookup(strokes)
        assert test == f'쏴{OPERATOR_ATTACH}'

    def test_initial_pp_medial_wo(self):
        strokes = ('ㅇㅂㅜㅓ',)
        test = lookup(strokes)
        assert test == f'뿨{OPERATOR_ATTACH}'

    def test_initial_h_medial_wae(self):
        strokes = ('ㅎㅗㅏㅣ',)
        test = lookup(strokes)
        assert test == f'홰{OPERATOR_ATTACH}'

    def test_initial_m_medial_we(self):
        strokes = ('ㅁㅜㅓㅣ',)
        test = lookup(strokes)
        assert test == f'뭬{OPERATOR_ATTACH}'

    def test_initial_ng_medial_o(self):
        strokes = ('ㅇㅣ',)
        with pytest.raises(KeyError):
            lookup(strokes)

    def test_medial_star(self):
        strokes = ('*',)
        with pytest.raises(KeyError):
            lookup(strokes)

    def test_medial_o(self):
        strokes = ('ㅗ',)
        test = lookup(strokes)
        assert test == f'오{OPERATOR_ATTACH}'

    def test_medial_a(self):
        strokes = ('ㅏ',)
        test = lookup(strokes)
        assert test == f'아{OPERATOR_ATTACH}'

    def test_medial_u(self):
        strokes = ('ㅜ',)
        test = lookup(strokes)
        assert test == f'우{OPERATOR_ATTACH}'

    def test_medial_eo(self):
        strokes = ('ㅓ',)
        test = lookup(strokes)
        assert test == f'어{OPERATOR_ATTACH}'

    def test_medial_i(self):
        strokes = ('ㅣ',)
        test = lookup(strokes)
        assert test == f'이{OPERATOR_ATTACH}'

    def test_medial_eu(self):
        strokes = ('ㅏㅓ',)
        test = lookup(strokes)
        assert test == f'으{OPERATOR_ATTACH}'

    def test_medial_ae(self):
        strokes = ('ㅏㅣ',)
        test = lookup(strokes)
        assert test == f'애{OPERATOR_ATTACH}'

    def test_medial_e(self):
        strokes = ('ㅓㅣ',)
        test = lookup(strokes)
        assert test == f'에{OPERATOR_ATTACH}'

    def test_medial_yo(self):
        strokes = ('ㅗ*',)
        test = lookup(strokes)
        assert test == f'요{OPERATOR_ATTACH}'

    def test_medial_ya(self):
        strokes = ('ㅏ*',)
        test = lookup(strokes)
        assert test == f'야{OPERATOR_ATTACH}'

    def test_medial_yu(self):
        strokes = ('ㅜ*',)
        test = lookup(strokes)
        assert test == f'유{OPERATOR_ATTACH}'

    def test_medial_yeo(self):
        strokes = ('*ㅓ',)
        test = lookup(strokes)
        assert test == f'여{OPERATOR_ATTACH}'

    def test_medial_yae(self):
        strokes = ('ㅏ*ㅓ',)
        test = lookup(strokes)
        assert test == f'얘{OPERATOR_ATTACH}'

    def test_medial_ye(self):
        strokes = ('ㅗㅓㅣ',)
        test = lookup(strokes)
        assert test == f'예{OPERATOR_ATTACH}'

    def test_medial_ui(self):
        strokes = ('ㅏㅓㅣ',)
        test = lookup(strokes)
        assert test == f'의{OPERATOR_ATTACH}'

    def test_medial_oe(self):
        strokes = ('ㅗㅣ',)
        test = lookup(strokes)
        assert test == f'외{OPERATOR_ATTACH}'

    def test_medial_wi(self):
        strokes = ('ㅜㅣ',)
        test = lookup(strokes)
        assert test == f'위{OPERATOR_ATTACH}'

    def test_medial_wa(self):
        strokes = ('ㅗㅏ',)
        test = lookup(strokes)
        assert test == f'와{OPERATOR_ATTACH}'

    def test_medial_wo(self):
        strokes = ('ㅜㅓ',)
        test = lookup(strokes)
        assert test == f'워{OPERATOR_ATTACH}'

    def test_medial_wae(self):
        strokes = ('ㅏㅣ',)
        test = lookup(strokes)
        assert test == f'애{OPERATOR_ATTACH}'

    def test_medial_we(self):
        strokes = ('ㅓㅣ',)
        test = lookup(strokes)
        assert test == f'에{OPERATOR_ATTACH}'

    def test_initial_ng_medial_o_final_m(self):
        strokes = ('ㅇㅣㅁ',)
        with pytest.raises(KeyError):
            lookup(strokes)

    def test_initial_h_medial_o_final_m(self):
        strokes = ('ㅎㅗㅁ',)
        test = lookup(strokes)
        assert test == f'홈{OPERATOR_ATTACH}'

    def test_initial_m_medial_a_final_j(self):
        strokes = ('ㅁㅏㅈ',)
        test = lookup(strokes)
        assert test == f'맞{OPERATOR_ATTACH}'

    def test_initial_g_medial_u_final_s(self):
        strokes = ('ㄱㅜㅅ',)
        test = lookup(strokes)
        assert test == f'굿{OPERATOR_ATTACH}'

    def test_initial_j_medial_eo_final_n(self):
        strokes = ('ㅈㅓㄴ',)
        test = lookup(strokes)
        assert test == f'전{OPERATOR_ATTACH}'

    def test_initial_n_medial_i_final_b(self):
        strokes = ('ㄴㅣㅂ',)
        test = lookup(strokes)
        assert test == f'닙{OPERATOR_ATTACH}'

    def test_initial_d_medial_eu_final_d(self):
        strokes = ('ㄷㅏㅓㄷ',)
        test = lookup(strokes)
        assert test == f'듣{OPERATOR_ATTACH}'

    def test_inintial_s_medial_ae_final_g(self):
        strokes = ('ㅅㅏㅣㄱ',)
        test = lookup(strokes)
        assert test == f'색{OPERATOR_ATTACH}'

    def test_initial_b_medial_e_final_r(self):
        strokes = ('ㅂㅓㅣㄹ',)
        test = lookup(strokes)
        assert test == f'벨{OPERATOR_ATTACH}'

    def test_initial_r_medial_yo_final_ng(self):
        strokes = ('ㄹㅗ*ㅇ',)
        test = lookup(strokes)
        assert test == f'룡{OPERATOR_ATTACH}'

    def test_initial_k_medial_ya_final_h(self):
        strokes = ('ㅎㄱㅏ*ㅎ',)
        test = lookup(strokes)
        assert test == f'컇{OPERATOR_ATTACH}'

    def test_initial_ch_medial_yu_final_ch(self):
        strokes = ('ㅎㅈㅜ*ㅎㅈ',)
        test = lookup(strokes)
        assert test == f'츛{OPERATOR_ATTACH}'

    def test_initial_t_medial_yeo_final_p(self):
        strokes = ('ㅎㄷ*ㅓㅎㅂ',)
        test = lookup(strokes)
        assert test == f'톂{OPERATOR_ATTACH}'

    def test_initial_t_medial_yae_final_t(self):
        strokes = ('ㅎㄷㅏ*ㅓㅎㄷ',)
        test = lookup(strokes)
        assert test == f'턭{OPERATOR_ATTACH}'

    def test_initial_p_medial_ye_final_k(self):
        strokes = ('ㅎㅂㅗㅓㅣㅎㄱ',)
        test = lookup(strokes)
        assert test == f'폨{OPERATOR_ATTACH}'

    def test_intitial_kk_medial_ui_final_ss(self):
        strokes = ('ㄱㅇㅏㅓㅣㅇㅅ',)
        test = lookup(strokes)
        assert test == f'끴{OPERATOR_ATTACH}'

    def test_initial_jj_medial_oe_final_kk(self):
        strokes = ('ㅈㅇㅗㅣㅇㄱ',)
        test = lookup(strokes)
        assert test == f'쬒{OPERATOR_ATTACH}'

    def test_initial_tt_medial_wi_final_gs(self):
        strokes = ('ㄷㅇㅜㅣㄱㅅ',)
        test = lookup(strokes)
        assert test == f'뛳{OPERATOR_ATTACH}'

    def test_initial_ss_medial_wa_final_nj(self):
        strokes = ('ㅇㅅㅗㅏㄴㅈ',)
        test = lookup(strokes)
        assert test == f'쏹{OPERATOR_ATTACH}'

    def test_initial_pp_medial_wo_final_nh(self):
        strokes = ('ㅇㅂㅜㅓㅎㄴ',)
        test = lookup(strokes)
        assert test == f'뿮{OPERATOR_ATTACH}'

    def test_initial_h_medial_wae_final_rg(self):
        strokes = ('ㅎㅗㅏㅣㄹㄱ',)
        test = lookup(strokes)
        assert test == f'홹{OPERATOR_ATTACH}'

    def test_initial_m_medial_we_final_rm(self):
        strokes = ('ㅁㅜㅓㅣㄹㅁ',)
        test = lookup(strokes)
        assert test == f'뭶{OPERATOR_ATTACH}'

    def test_initial_h_medial_a_final_rb(self):
        strokes = ('ㅎㅏㄹㅂ',)
        test = lookup(strokes)
        assert test == f'핣{OPERATOR_ATTACH}'

    def test_initial_h_medial_a_final_rs(self):
        strokes = ('ㅎㅏㄹㅅ',)
        test = lookup(strokes)
        assert test == f'핤{OPERATOR_ATTACH}'

    def test_initial_h_medial_a_final_rt(self):
        strokes = ('ㅎㅏㅎㄹㄷ',)
        test = lookup(strokes)
        assert test == f'핥{OPERATOR_ATTACH}'

    def test_initial_h_medial_a_final_rp(self):
        strokes = ('ㅎㅏㅎㄹㅂ',)
        test = lookup(strokes)
        assert test == f'핦{OPERATOR_ATTACH}'

    def test_initial_h_medial_a_final_rh(self):
        strokes = ('ㅎㅏㅎㄹ',)
        test = lookup(strokes)
        assert test == f'핧{OPERATOR_ATTACH}'

    def test_initial_h_medial_a_final_bs(self):
        strokes = ('ㅎㅏㅂㅅ',)
        test = lookup(strokes)
        assert test == f'핪{OPERATOR_ATTACH}'

class TestLookupConjugations(object):
    ''' Test conjugation cases of lookup '''

    def test_nda(self):
        strokes = ('ㄴㅣㄷㄴ',)
        test = lookup(strokes)
        assert test == f'닌다{OPERATOR_ATTACH}'

    def test_bnida(self):
        strokes = ('ㄴㅣㅂㄴ',)
        test = lookup(strokes)
        assert test == f'닙니다{OPERATOR_ATTACH}'

    def test_ssseubnida(self):
        strokes = ('ㄴㅣㅂㄴㅅㅈ',)
        test = lookup(strokes)
        assert test == f'닜습니다{OPERATOR_ATTACH}'

    def test_ssda(self):
        strokes = ('ㄴㅣㄷㅅ',)
        test = lookup(strokes)
        assert test == f'닜다{OPERATOR_ATTACH}'

    def test_bnikka(self):
        strokes = ('ㄴㅣㅂㄴㅅ',)
        test = lookup(strokes)
        assert test == f'닙니까{OPERATOR_ATTACH}'

    def test_ssseubnikka(self):
        strokes = ('ㄴㅣㅂㄴㅅㅁ',)
        test = lookup(strokes)
        assert test == f'닜습니까{OPERATOR_ATTACH}'

    def test_bsida(self):
        strokes = ('ㄴㅣㄷㅂㅅ',)
        test = lookup(strokes)
        assert test == f'닙시다{OPERATOR_ATTACH}'

    def test_ngun(self):
        strokes = ('ㄴㅣㅇㄴ',)
        test = lookup(strokes)
        assert test == f'니운{OPERATOR_ATTACH}'

    def test_ngur(self):
        strokes = ('ㄴㅣㅇㄹ',)
        test = lookup(strokes)
        assert test == f'니울{OPERATOR_ATTACH}'

    def test_ngum(self):
        strokes = ('ㄴㅣㅇㅁ',)
        test = lookup(strokes)
        assert test == f'니움{OPERATOR_ATTACH}'

    def test_nga(self):
        strokes = ('ㄴㅣㄱㄴ',)
        test = lookup(strokes)
        assert test == f'닌가{OPERATOR_ATTACH}'

    def test_ndago(self):
        strokes = ('ㄴㅣㄱㄷㄴ',)
        test = lookup(strokes)
        assert test == f'닌다고{OPERATOR_ATTACH}'

    def test_nji(self):
        strokes = ('ㄴㅣㄱㄴㅈ',)
        test = lookup(strokes)
        assert test == f'닌지{OPERATOR_ATTACH}'

    def test_r_ttae(self):
        strokes = ('ㄴㅣㄹㄷ',)
        test = lookup(strokes)
        assert test == f'닐 때{OPERATOR_ATTACH}'

    # TODO: This conflicts with 닔 type of syllables.
    #       Need to make alternate rule?
    # def test_r_su(self):
    #     strokes = ('ㄴㅣㄹㅅ',)
    #     test = lookup(strokes)
    #     assert test == f'닐 수{OPERATOR_ATTACH}'

    def test_rji(self):
        strokes = ('ㄴㅣㄹㅈ',)
        test = lookup(strokes)
        assert test == f'닐지{OPERATOR_ATTACH}'

    def test_rkka(self):
        strokes = ('ㄴㅣㄹㄱㅁ',)
        test = lookup(strokes)
        assert test == f'닐까{OPERATOR_ATTACH}'

    def test_bda(self):
        strokes = ('ㄴㅣㄷㅂ',)
        test = lookup(strokes)
        assert test == f'닙다{OPERATOR_ATTACH}'

    def test_bge(self):
        strokes = ('ㄴㅣㄱㅂ',)
        test = lookup(strokes)
        assert test == f'닙게{OPERATOR_ATTACH}'

    def test_bgo(self):
        strokes = ('ㄴㅣㅂㅅㅈ',)
        test = lookup(strokes)
        assert test == f'닙고{OPERATOR_ATTACH}'

    def test_bji(self):
        strokes = ('ㄴㅣㅂㅈ',)
        test = lookup(strokes)
        assert test == f'닙지{OPERATOR_ATTACH}'

    def test_bjiman(self):
        strokes = ('ㄴㅣㅂㅈㅁ',)
        test = lookup(strokes)
        assert test == f'닙지만{OPERATOR_ATTACH}'

class TestLookupParticles(object):
    ''' Test particle cases of lookup '''

    def test_ga(self):
        strokes = ('ㅁㅏㅓㄱㄷ',)
        test = lookup(strokes)
        assert test == f'므가{OPERATOR_ATTACH}'

    def test_ge(self):
        strokes = ('ㅁㅏㅓㅅㅈ',)
        test = lookup(strokes)
        assert test == f'므게{OPERATOR_ATTACH}'

    def test_go(self):
        strokes = ('ㅁㅏㅓㅇㄹㄱㄷ',)
        test = lookup(strokes)
        assert test == f'므고{OPERATOR_ATTACH}'

    def test_da(self):
        strokes = ('ㅁㅏㅓㄷㅈ',)
        test = lookup(strokes)
        assert test == f'므다{OPERATOR_ATTACH}'

    def test_neun(self):
        strokes = ('ㅁㅏㅓㄴㅅㅈㅁ',)
        test = lookup(strokes)
        assert test == f'므는{OPERATOR_ATTACH}'

    def test_ra(self):
        strokes = ('ㅁㅏㅓㅎㅇㄹ',)
        test = lookup(strokes)
        assert test == f'므라{OPERATOR_ATTACH}'

    def test_ngeo(self):
        strokes = ('ㅁㅏㅓㅇㄹㄱ',)
        test = lookup(strokes)
        assert test == f'므어{OPERATOR_ATTACH}'

    def test_na(self):
        strokes = ('ㅁㅏㅓㄹㄴㅅ',)
        test = lookup(strokes)
        assert test == f'므나{OPERATOR_ATTACH}'

    def test_ni(self):
        strokes = ('ㅁㅏㅓㄴㅅ',)
        test = lookup(strokes)
        assert test == f'므니{OPERATOR_ATTACH}'

    def test_nikka(self):
        strokes = ('ㅁㅏㅓㄴㅅㅈ',)
        test = lookup(strokes)
        assert test == f'므니까{OPERATOR_ATTACH}'

    def test_myeon(self):
        strokes = ('ㅁㅏㅓㄴㅁ',)
        test = lookup(strokes)
        assert test == f'므면{OPERATOR_ATTACH}'

    def test_meonseo(self):
        strokes = ('ㅁㅏㅓㄴㅅㅁ',)
        test = lookup(strokes)
        assert test == f'므면서{OPERATOR_ATTACH}'

    def test_do(self):
        strokes = ('ㅁㅏㅓㄷㅁ',)
        test = lookup(strokes)
        assert test == f'므도{OPERATOR_ATTACH}'

    def test_dorog(self):
        strokes = ('ㅁㅏㅓㄹㄱㄷ',)
        test = lookup(strokes)
        assert test == f'므도록{OPERATOR_ATTACH}'

    def test_ji(self):
        strokes = ('ㅁㅏㅓㄱㅈ',)
        test = lookup(strokes)
        assert test == f'므지{OPERATOR_ATTACH}'

    def test_jiman(self):
        strokes = ('ㅁㅏㅓㅈㅁ',)
        test = lookup(strokes)
        assert test == f'므지만{OPERATOR_ATTACH}'

    def test_buteo(self):
        strokes = ('ㅁㅏㅓㅎㄷㅂ',)
        test = lookup(strokes)
        assert test == f'므부터{OPERATOR_ATTACH}'
