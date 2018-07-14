"""Unit tests for the base dictionary."""

import pytest

from plover_korean.system.cas.dictionaries.ko_cas_base import (
    lookup,
    OPERATOR_ATTACH
)


class TestLookup(object):
    """Tests the base cases of lookup."""

    def test_length_zero(self):
        strokes = ()
        with pytest.raises(KeyError):
            lookup(strokes)

    def test_length_one(self):
        strokes = ('ㄴㅣㄱ',)
        text = lookup(strokes)
        assert text == f'닉{OPERATOR_ATTACH}'

    def test_length_two(self):
        strokes = ('ㄴㅣㄱ', 'ㄴㅣㄱ')
        with pytest.raises(KeyError):
            lookup(strokes)

    def test_steno_order_wrong(self):
        strokes = ('ㅈㅎㅏ',)
        with pytest.raises(KeyError):
            lookup(strokes)

    def test_contains_english(self):
        strokes = ('HR',)
        with pytest.raises(KeyError):
            lookup(strokes)

    def test_contains_numbers(self):
        strokes = ('ㅎㅏ8',)
        with pytest.raises(KeyError):
            lookup(strokes)


class TestLookupSyllableBlocks(object):
    """Tests syllable block construction cases of lookup."""

    def test_initial_h_medial_o(self):
        strokes = ('ㅎㅗ',)
        text = lookup(strokes)
        assert text == f'호{OPERATOR_ATTACH}'

    def test_initial_m_medial_a(self):
        strokes = ('ㅁㅏ',)
        text = lookup(strokes)
        assert text == f'마{OPERATOR_ATTACH}'

    def test_initial_g_medial_u(self):
        strokes = ('ㄱㅜ',)
        text = lookup(strokes)
        assert text == f'구{OPERATOR_ATTACH}'

    def test_initial_j_medial_eo(self):
        strokes = ('ㅈㅓ',)
        text = lookup(strokes)
        assert text == f'저{OPERATOR_ATTACH}'

    def test_initial_n_medial_i(self):
        strokes = ('ㄴㅣ',)
        text = lookup(strokes)
        assert text == f'니{OPERATOR_ATTACH}'

    def test_initial_d_medial_eu(self):
        strokes = ('ㄷㅏㅓ',)
        text = lookup(strokes)
        assert text == f'드{OPERATOR_ATTACH}'

    def test_inintial_s_medial_ae(self):
        strokes = ('ㅅㅏㅣ',)
        text = lookup(strokes)
        assert text == f'새{OPERATOR_ATTACH}'

    def test_initial_b_medial_e(self):
        strokes = ('ㅂㅓㅣ',)
        text = lookup(strokes)
        assert text == f'베{OPERATOR_ATTACH}'

    def test_initial_r_medial_yo(self):
        strokes = ('ㄹㅗ*',)
        text = lookup(strokes)
        assert text == f'료{OPERATOR_ATTACH}'

    def test_initial_k_medial_ya(self):
        strokes = ('ㅎㄱㅏ*',)
        text = lookup(strokes)
        assert text == f'캬{OPERATOR_ATTACH}'

    def test_initial_ch_medial_yu(self):
        strokes = ('ㅎㅈㅜ*',)
        text = lookup(strokes)
        assert text == f'츄{OPERATOR_ATTACH}'

    def test_initial_t_medial_yeo(self):
        strokes = ('ㅎㄷ*ㅓ',)
        text = lookup(strokes)
        assert text == f'텨{OPERATOR_ATTACH}'

    def test_initial_t_medial_yae(self):
        strokes = ('ㅎㄷㅏ*ㅓ',)
        text = lookup(strokes)
        assert text == f'턔{OPERATOR_ATTACH}'

    def test_initial_p_medial_ye(self):
        strokes = ('ㅎㅂㅗㅓㅣ',)
        text = lookup(strokes)
        assert text == f'폐{OPERATOR_ATTACH}'

    def test_intitial_kk_medial_ui(self):
        strokes = ('ㄱㅇㅏㅓㅣ',)
        text = lookup(strokes)
        assert text == f'끠{OPERATOR_ATTACH}'

    def test_initial_jj_medial_oe(self):
        strokes = ('ㅈㅇㅗㅣ',)
        text = lookup(strokes)
        assert text == f'쬐{OPERATOR_ATTACH}'

    def test_initial_tt_medial_wi(self):
        strokes = ('ㄷㅇㅜㅣ',)
        text = lookup(strokes)
        assert text == f'뛰{OPERATOR_ATTACH}'

    def test_initial_ss_medial_wa(self):
        strokes = ('ㅇㅅㅗㅏ',)
        text = lookup(strokes)
        assert text == f'쏴{OPERATOR_ATTACH}'

    def test_initial_pp_medial_wo(self):
        strokes = ('ㅇㅂㅜㅓ',)
        text = lookup(strokes)
        assert text == f'뿨{OPERATOR_ATTACH}'

    def test_initial_h_medial_wae(self):
        strokes = ('ㅎㅗㅏㅣ',)
        text = lookup(strokes)
        assert text == f'홰{OPERATOR_ATTACH}'

    def test_initial_m_medial_we(self):
        strokes = ('ㅁㅜㅓㅣ',)
        text = lookup(strokes)
        assert text == f'뭬{OPERATOR_ATTACH}'

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
        text = lookup(strokes)
        assert text == f'오{OPERATOR_ATTACH}'

    def test_medial_a(self):
        strokes = ('ㅏ',)
        text = lookup(strokes)
        assert text == f'아{OPERATOR_ATTACH}'

    def test_medial_u(self):
        strokes = ('ㅜ',)
        text = lookup(strokes)
        assert text == f'우{OPERATOR_ATTACH}'

    def test_medial_eo(self):
        strokes = ('ㅓ',)
        text = lookup(strokes)
        assert text == f'어{OPERATOR_ATTACH}'

    def test_medial_i(self):
        strokes = ('ㅣ',)
        text = lookup(strokes)
        assert text == f'이{OPERATOR_ATTACH}'

    def test_medial_eu(self):
        strokes = ('ㅏㅓ',)
        text = lookup(strokes)
        assert text == f'으{OPERATOR_ATTACH}'

    def test_medial_ae(self):
        strokes = ('ㅏㅣ',)
        text = lookup(strokes)
        assert text == f'애{OPERATOR_ATTACH}'

    def test_medial_e(self):
        strokes = ('ㅓㅣ',)
        text = lookup(strokes)
        assert text == f'에{OPERATOR_ATTACH}'

    def test_medial_yo(self):
        strokes = ('ㅗ*',)
        text = lookup(strokes)
        assert text == f'요{OPERATOR_ATTACH}'

    def test_medial_ya(self):
        strokes = ('ㅏ*',)
        text = lookup(strokes)
        assert text == f'야{OPERATOR_ATTACH}'

    def test_medial_yu(self):
        strokes = ('ㅜ*',)
        text = lookup(strokes)
        assert text == f'유{OPERATOR_ATTACH}'

    def test_medial_yeo(self):
        strokes = ('*ㅓ',)
        text = lookup(strokes)
        assert text == f'여{OPERATOR_ATTACH}'

    def test_medial_yae(self):
        strokes = ('ㅏ*ㅓ',)
        text = lookup(strokes)
        assert text == f'얘{OPERATOR_ATTACH}'

    def test_medial_ye(self):
        strokes = ('ㅗㅓㅣ',)
        text = lookup(strokes)
        assert text == f'예{OPERATOR_ATTACH}'

    def test_medial_ui(self):
        strokes = ('ㅏㅓㅣ',)
        text = lookup(strokes)
        assert text == f'의{OPERATOR_ATTACH}'

    def test_medial_oe(self):
        strokes = ('ㅗㅣ',)
        text = lookup(strokes)
        assert text == f'외{OPERATOR_ATTACH}'

    def test_medial_wi(self):
        strokes = ('ㅜㅣ',)
        text = lookup(strokes)
        assert text == f'위{OPERATOR_ATTACH}'

    def test_medial_wa(self):
        strokes = ('ㅗㅏ',)
        text = lookup(strokes)
        assert text == f'와{OPERATOR_ATTACH}'

    def test_medial_wo(self):
        strokes = ('ㅜㅓ',)
        text = lookup(strokes)
        assert text == f'워{OPERATOR_ATTACH}'

    def test_medial_wae(self):
        strokes = ('ㅏㅣ',)
        text = lookup(strokes)
        assert text == f'애{OPERATOR_ATTACH}'

    def test_medial_we(self):
        strokes = ('ㅓㅣ',)
        text = lookup(strokes)
        assert text == f'에{OPERATOR_ATTACH}'

    def test_initial_ng_medial_o_final_m(self):
        strokes = ('ㅇㅣㅁ',)
        with pytest.raises(KeyError):
            lookup(strokes)

    def test_initial_h_medial_o_final_m(self):
        strokes = ('ㅎㅗㅁ',)
        text = lookup(strokes)
        assert text == f'홈{OPERATOR_ATTACH}'

    def test_initial_m_medial_a_final_j(self):
        strokes = ('ㅁㅏㅈ',)
        text = lookup(strokes)
        assert text == f'맞{OPERATOR_ATTACH}'

    def test_initial_g_medial_u_final_s(self):
        strokes = ('ㄱㅜㅅ',)
        text = lookup(strokes)
        assert text == f'굿{OPERATOR_ATTACH}'

    def test_initial_j_medial_eo_final_n(self):
        strokes = ('ㅈㅓㄴ',)
        text = lookup(strokes)
        assert text == f'전{OPERATOR_ATTACH}'

    def test_initial_n_medial_i_final_b(self):
        strokes = ('ㄴㅣㅂ',)
        text = lookup(strokes)
        assert text == f'닙{OPERATOR_ATTACH}'

    def test_initial_d_medial_eu_final_d(self):
        strokes = ('ㄷㅏㅓㄷ',)
        text = lookup(strokes)
        assert text == f'듣{OPERATOR_ATTACH}'

    def test_inintial_s_medial_ae_final_g(self):
        strokes = ('ㅅㅏㅣㄱ',)
        text = lookup(strokes)
        assert text == f'색{OPERATOR_ATTACH}'

    def test_initial_b_medial_e_final_r(self):
        strokes = ('ㅂㅓㅣㄹ',)
        text = lookup(strokes)
        assert text == f'벨{OPERATOR_ATTACH}'

    def test_initial_r_medial_yo_final_ng(self):
        strokes = ('ㄹㅗ*ㅇ',)
        text = lookup(strokes)
        assert text == f'룡{OPERATOR_ATTACH}'

    def test_initial_k_medial_ya_final_h(self):
        strokes = ('ㅎㄱㅏ*ㅎ',)
        text = lookup(strokes)
        assert text == f'컇{OPERATOR_ATTACH}'

    def test_initial_ch_medial_yu_final_ch(self):
        strokes = ('ㅎㅈㅜ*ㅎㅈ',)
        text = lookup(strokes)
        assert text == f'츛{OPERATOR_ATTACH}'

    def test_initial_t_medial_yeo_final_p(self):
        strokes = ('ㅎㄷ*ㅓㅎㅂ',)
        text = lookup(strokes)
        assert text == f'톂{OPERATOR_ATTACH}'

    def test_initial_t_medial_yae_final_t(self):
        strokes = ('ㅎㄷㅏ*ㅓㅎㄷ',)
        text = lookup(strokes)
        assert text == f'턭{OPERATOR_ATTACH}'

    def test_initial_p_medial_ye_final_k(self):
        strokes = ('ㅎㅂㅗㅓㅣㅎㄱ',)
        text = lookup(strokes)
        assert text == f'폨{OPERATOR_ATTACH}'

    def test_intitial_kk_medial_ui_final_ss(self):
        strokes = ('ㄱㅇㅏㅓㅣㅇㅅ',)
        text = lookup(strokes)
        assert text == f'끴{OPERATOR_ATTACH}'

    def test_initial_jj_medial_oe_final_kk(self):
        strokes = ('ㅈㅇㅗㅣㅇㄱ',)
        text = lookup(strokes)
        assert text == f'쬒{OPERATOR_ATTACH}'

    def test_initial_tt_medial_wi_final_gs(self):
        strokes = ('ㄷㅇㅜㅣㄱㅅ',)
        text = lookup(strokes)
        assert text == f'뛳{OPERATOR_ATTACH}'

    def test_initial_ss_medial_wa_final_nj(self):
        strokes = ('ㅇㅅㅗㅏㄴㅈ',)
        text = lookup(strokes)
        assert text == f'쏹{OPERATOR_ATTACH}'

    def test_initial_pp_medial_wo_final_nh(self):
        strokes = ('ㅇㅂㅜㅓㅎㄴ',)
        text = lookup(strokes)
        assert text == f'뿮{OPERATOR_ATTACH}'

    def test_initial_h_medial_wae_final_rg(self):
        strokes = ('ㅎㅗㅏㅣㄹㄱ',)
        text = lookup(strokes)
        assert text == f'홹{OPERATOR_ATTACH}'

    def test_initial_m_medial_we_final_rm(self):
        strokes = ('ㅁㅜㅓㅣㄹㅁ',)
        text = lookup(strokes)
        assert text == f'뭶{OPERATOR_ATTACH}'

    def test_initial_h_medial_a_final_rb(self):
        strokes = ('ㅎㅏㄹㅂ',)
        text = lookup(strokes)
        assert text == f'핣{OPERATOR_ATTACH}'

    def test_initial_h_medial_a_final_rs(self):
        strokes = ('ㅎㅏㄹㅅ',)
        text = lookup(strokes)
        assert text == f'핤{OPERATOR_ATTACH}'

    def test_initial_h_medial_a_final_rt(self):
        strokes = ('ㅎㅏㅎㄹㄷ',)
        text = lookup(strokes)
        assert text == f'핥{OPERATOR_ATTACH}'

    def test_initial_h_medial_a_final_rp(self):
        strokes = ('ㅎㅏㅎㄹㅂ',)
        text = lookup(strokes)
        assert text == f'핦{OPERATOR_ATTACH}'

    def test_initial_h_medial_a_final_rh(self):
        strokes = ('ㅎㅏㅎㄹ',)
        text = lookup(strokes)
        assert text == f'핧{OPERATOR_ATTACH}'

    def test_initial_h_medial_a_final_bs(self):
        strokes = ('ㅎㅏㅂㅅ',)
        text = lookup(strokes)
        assert text == f'핪{OPERATOR_ATTACH}'


class TestLookupConjugations(object):
    """Tests conjugation cases of lookup."""

    def test_nda(self):
        strokes = ('ㄴㅣㄷㄴ',)
        text = lookup(strokes)
        assert text == f'닌다{OPERATOR_ATTACH}'

    def test_bnida(self):
        strokes = ('ㄴㅣㅂㄴ',)
        text = lookup(strokes)
        assert text == f'닙니다{OPERATOR_ATTACH}'

    def test_ssseubnida(self):
        strokes = ('ㄴㅣㅂㄴㅅㅈ',)
        text = lookup(strokes)
        assert text == f'닜습니다{OPERATOR_ATTACH}'

    def test_ssda(self):
        strokes = ('ㄴㅣㄷㅅ',)
        text = lookup(strokes)
        assert text == f'닜다{OPERATOR_ATTACH}'

    def test_bnikka(self):
        strokes = ('ㄴㅣㅂㄴㅅ',)
        text = lookup(strokes)
        assert text == f'닙니까{OPERATOR_ATTACH}'

    def test_ssseubnikka(self):
        strokes = ('ㄴㅣㅂㄴㅅㅁ',)
        text = lookup(strokes)
        assert text == f'닜습니까{OPERATOR_ATTACH}'

    def test_bsida(self):
        strokes = ('ㄴㅣㄷㅂㅅ',)
        text = lookup(strokes)
        assert text == f'닙시다{OPERATOR_ATTACH}'

    def test_ngun(self):
        strokes = ('ㄴㅣㅇㄴ',)
        text = lookup(strokes)
        assert text == f'니운{OPERATOR_ATTACH}'

    def test_ngur(self):
        strokes = ('ㄴㅣㅇㄹ',)
        text = lookup(strokes)
        assert text == f'니울{OPERATOR_ATTACH}'

    def test_ngum(self):
        strokes = ('ㄴㅣㅇㅁ',)
        text = lookup(strokes)
        assert text == f'니움{OPERATOR_ATTACH}'

    def test_nga(self):
        strokes = ('ㄴㅣㄱㄴ',)
        text = lookup(strokes)
        assert text == f'닌가{OPERATOR_ATTACH}'

    def test_ndago(self):
        strokes = ('ㄴㅣㄱㄷㄴ',)
        text = lookup(strokes)
        assert text == f'닌다고{OPERATOR_ATTACH}'

    def test_nji(self):
        strokes = ('ㄴㅣㄱㄴㅈ',)
        text = lookup(strokes)
        assert text == f'닌지{OPERATOR_ATTACH}'

    def test_r_ttae(self):
        strokes = ('ㄴㅣㄹㄷ',)
        text = lookup(strokes)
        assert text == f'닐 때{OPERATOR_ATTACH}'

    # TODO: This conflicts with 닔 type of syllables.
    #       Need to make alternate rule?
    # def test_r_su(self):
    #     strokes = ('ㄴㅣㄹㅅ',)
    #     text = lookup(strokes)
    #     assert text == f'닐 수{OPERATOR_ATTACH}'

    def test_rji(self):
        strokes = ('ㄴㅣㄹㅈ',)
        text = lookup(strokes)
        assert text == f'닐지{OPERATOR_ATTACH}'

    def test_rkka(self):
        strokes = ('ㄴㅣㄹㄱㅁ',)
        text = lookup(strokes)
        assert text == f'닐까{OPERATOR_ATTACH}'

    def test_bda(self):
        strokes = ('ㄴㅣㄷㅂ',)
        text = lookup(strokes)
        assert text == f'닙다{OPERATOR_ATTACH}'

    def test_bge(self):
        strokes = ('ㄴㅣㄱㅂ',)
        text = lookup(strokes)
        assert text == f'닙게{OPERATOR_ATTACH}'

    def test_bgo(self):
        strokes = ('ㄴㅣㅂㅅㅈ',)
        text = lookup(strokes)
        assert text == f'닙고{OPERATOR_ATTACH}'

    def test_bji(self):
        strokes = ('ㄴㅣㅂㅈ',)
        text = lookup(strokes)
        assert text == f'닙지{OPERATOR_ATTACH}'

    def test_bjiman(self):
        strokes = ('ㄴㅣㅂㅈㅁ',)
        text = lookup(strokes)
        assert text == f'닙지만{OPERATOR_ATTACH}'


class TestLookupParticles(object):
    """Tests particle cases of lookup."""

    def test_ga(self):
        strokes = ('ㅁㅏㅓㄱㄷ',)
        text = lookup(strokes)
        assert text == f'므가{OPERATOR_ATTACH}'

    def test_ge(self):
        strokes = ('ㅁㅏㅓㅅㅈ',)
        text = lookup(strokes)
        assert text == f'므게{OPERATOR_ATTACH}'

    def test_go(self):
        strokes = ('ㅁㅏㅓㅇㄹㄱㄷ',)
        text = lookup(strokes)
        assert text == f'므고{OPERATOR_ATTACH}'

    def test_da(self):
        strokes = ('ㅁㅏㅓㄷㅈ',)
        text = lookup(strokes)
        assert text == f'므다{OPERATOR_ATTACH}'

    def test_neun(self):
        strokes = ('ㅁㅏㅓㄴㅅㅈㅁ',)
        text = lookup(strokes)
        assert text == f'므는{OPERATOR_ATTACH}'

    def test_ra(self):
        strokes = ('ㅁㅏㅓㅎㅇㄹ',)
        text = lookup(strokes)
        assert text == f'므라{OPERATOR_ATTACH}'

    def test_ngeo(self):
        strokes = ('ㅁㅏㅓㅇㄹㄱ',)
        text = lookup(strokes)
        assert text == f'므어{OPERATOR_ATTACH}'

    def test_na(self):
        strokes = ('ㅁㅏㅓㄹㄴㅅ',)
        text = lookup(strokes)
        assert text == f'므나{OPERATOR_ATTACH}'

    def test_ni(self):
        strokes = ('ㅁㅏㅓㄴㅅ',)
        text = lookup(strokes)
        assert text == f'므니{OPERATOR_ATTACH}'

    def test_nikka(self):
        strokes = ('ㅁㅏㅓㄴㅅㅈ',)
        text = lookup(strokes)
        assert text == f'므니까{OPERATOR_ATTACH}'

    def test_myeon(self):
        strokes = ('ㅁㅏㅓㄴㅁ',)
        text = lookup(strokes)
        assert text == f'므면{OPERATOR_ATTACH}'

    def test_meonseo(self):
        strokes = ('ㅁㅏㅓㄴㅅㅁ',)
        text = lookup(strokes)
        assert text == f'므면서{OPERATOR_ATTACH}'

    def test_do(self):
        strokes = ('ㅁㅏㅓㄷㅁ',)
        text = lookup(strokes)
        assert text == f'므도{OPERATOR_ATTACH}'

    def test_dorog(self):
        strokes = ('ㅁㅏㅓㄹㄱㄷ',)
        text = lookup(strokes)
        assert text == f'므도록{OPERATOR_ATTACH}'

    def test_ji(self):
        strokes = ('ㅁㅏㅓㄱㅈ',)
        text = lookup(strokes)
        assert text == f'므지{OPERATOR_ATTACH}'

    def test_jiman(self):
        strokes = ('ㅁㅏㅓㅈㅁ',)
        text = lookup(strokes)
        assert text == f'므지만{OPERATOR_ATTACH}'

    def test_buteo(self):
        strokes = ('ㅁㅏㅓㅎㄷㅂ',)
        text = lookup(strokes)
        assert text == f'므부터{OPERATOR_ATTACH}'
