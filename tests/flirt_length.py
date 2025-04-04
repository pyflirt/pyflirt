import pytest
from pyflirt.ar_flirt import ar_flirt
from pyflirt.bn_flirt import bn_flirt
from pyflirt.bg_flirt import bg_flirt
from pyflirt.hr_flirt import hr_flirt
from pyflirt.cs_flirt import cs_flirt
from pyflirt.da_flirt import da_flirt
from pyflirt.nl_flirt import nl_flirt
from pyflirt.en_flirt import en_flirt
from pyflirt.et_flirt import et_flirt
from pyflirt.tl_flirt import tl_flirt
from pyflirt.fi_flirt import fi_flirt
from pyflirt.fr_flirt import fr_flirt
from pyflirt.de_flirt import de_flirt
from pyflirt.el_flirt import el_flirt
from pyflirt.he_flirt import he_flirt
from pyflirt.hi_flirt import hi_flirt
from pyflirt.hu_flirt import hu_flirt
from pyflirt.id_flirt import id_flirt
from pyflirt.it_flirt import it_flirt
from pyflirt.ja_flirt import ja_flirt
from pyflirt.kn_flirt import kn_flirt
from pyflirt.ko_flirt import ko_flirt
from pyflirt.lv_flirt import lv_flirt
from pyflirt.lt_flirt import lt_flirt
from pyflirt.ms_flirt import ms_flirt
from pyflirt.ml_flirt import ml_flirt
from pyflirt.mr_flirt import mr_flirt
from pyflirt.pl_flirt import pl_flirt
from pyflirt.pt_flirt import pt_flirt
from pyflirt.pa_flirt import pa_flirt
from pyflirt.fa_flirt import fa_flirt
from pyflirt.ro_flirt import ro_flirt
from pyflirt.ru_flirt import ru_flirt
from pyflirt.sr_flirt import sr_flirt
from pyflirt.sk_flirt import sk_flirt
from pyflirt.es_flirt import es_flirt
from pyflirt.sv_flirt import sv_flirt
from pyflirt.ta_flirt import ta_flirt
from pyflirt.te_flirt import te_flirt
from pyflirt.th_flirt import th_flirt
from pyflirt.tr_flirt import tr_flirt
from pyflirt.uk_flirt import uk_flirt
from pyflirt.ur_flirt import ur_flirt
from pyflirt.vi_flirt import vi_flirt

MAX_LENGTH = 200

flirt_sets = [
    ar_flirt,
    bn_flirt,
    bg_flirt,
    hr_flirt,
    cs_flirt,
    da_flirt,
    nl_flirt,
    en_flirt,
    et_flirt,
    tl_flirt,
    fi_flirt,
    fr_flirt,
    de_flirt,
    el_flirt,
    he_flirt,
    hi_flirt,
    hu_flirt,
    id_flirt,
    it_flirt,
    ja_flirt,
    kn_flirt,
    ko_flirt,
    lv_flirt,
    lt_flirt,
    ms_flirt,
    ml_flirt,
    mr_flirt,
    pl_flirt,
    pt_flirt,
    pa_flirt,
    fa_flirt,
    ro_flirt,
    ru_flirt,
    sr_flirt,
    sk_flirt,
    es_flirt,
    sv_flirt,
    ta_flirt,
    te_flirt,
    th_flirt,
    tr_flirt,
    uk_flirt,
    ur_flirt,
    vi_flirt,
]

@pytest.mark.parametrize("flirt_set", flirt_sets)
def test_flirt_length(flirt_set):
    """
    Ensures each flirt line in the 'all' type stays under MAX_LENGTH characters.
    """
    for flirt in flirt_set.get("all", []):
        assert isinstance(flirt, str), "Flirt should be a string"
        assert len(flirt) <= MAX_LENGTH, f"Flirt too long: {flirt}"
