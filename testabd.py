from ADB import AutoDatabank
from ADB import set_ROF
from ADB import set_pause
from random import choice

set_ROF(False)
set_pause(0.2, 0.3)
aa = AutoDatabank(zhanghao=2, tmall_global=False, purchase_Behaviour='dp')

aa.yybp_order = 1
aa.ppld_order = 1
aa.ppld_order = 2
aa.mxdp_order = 2
aa.zszw_order = 2

ts = '2019-1-1'
te = '2019-1-2'


def runa():
    aa.qll(12, ts, te, choice([1, 2, 3]))

    aa.ss('lccc,lccc2', ts, te, jbc=choice([1, 2, 3]))

    aa.ud([1, 1], ts, te, action=2)
    aa.ykgg([1, 1], ts, te, action=1)
    aa.yybp([1, 1], ts, te, action=2, jbc=choice([1, 2, 3]))
    aa.ppld([1, 1], ts, te, action=1, jbc=choice([1, 2, 3]))
    aa.ppzq([1, 1], ts, te, action=2, jbc=choice([1, 2, 3]))
    aa.mxdp([1, 1], ts, te, action=2, jbc=choice([1, 2, 3]))
    aa.zszw([1, 1], ts, te, action=1, jbc=choice([1, 2, 3]))
    aa.pphysgg([1, 1], ts, te, action=1, jbc=choice([1, 2, 3]))
    aa.yyy([1, 1], ts, te, action=1, jbc=choice([1, 2, 3]))

    aa.pph(1, 1, ts, te, jbc=choice([1, 2, 3]))
    aa.pph(1, 2, ts, te, jbc=choice([1, 2, 3]))
    aa.pph(2, 1, ts, te, jbc=choice([1, 2, 3]))
    aa.pph(2, 2, ts, te, jbc=choice([1, 2, 3]))

    aa.tbtt(choice([2, 4, 5]), ts, te, jbc=choice([1, 2, 3]))
    aa.yhh(2, ts, te, jbc=choice([1, 2, 3]))
    aa.bmqd(1, ts, te, jbc=choice([1, 2, 3]))
    aa.cnxh(1, ts, te, jbc=choice([1, 2, 3]))
    aa.shyjs(2, ts, te, jbc=choice([1, 2, 3]))
    aa.zb(1, ts, te, jbc=choice([1, 2, 3]))
    aa.wt(choice([1, 3, 4, 5]), ts, te, jbc=choice([1, 2, 3]))

    aa.mrhd(1, ts, te, jbc=choice([1, 2, 3]))
    aa.cjppr(1, ts, te, jbc=choice([1, 2, 3]))
    aa.hdb(1, 2, ts, te, jbc=choice([1, 2, 3]))
    aa.thllb(2, 1, ts, te, jbc=choice([1, 2, 3]))
    aa.jhs(2, ts, te, jbc=choice([1, 2, 3]))
    aa.syzx(2, ts, te, jbc=choice([1, 2, 3]))
    aa.tqg(1, ts, te, jbc=choice([1, 2, 3]))
    aa.hjr(1, ts, te, jbc=choice([1, 2, 3]))

aa.cp()
aa.zdy('S2-1107竞品词xX曝进预购')
aa.zdy('S2-1107竞品词xX曝进预购')
aa.zdy('S2-1107竞品词xX曝进预购')