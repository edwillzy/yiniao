from django.db import models

# Create your models here.
class personalInfo(models.Model):
    # 姓名
    xm = models.CharField(max_length=32,primary_key=True)
    # 英文全名
    ywqm = models.CharField(max_length=32)
    # 英文简名
    ywjm = models.CharField(max_length=32)
    # 性别
    xb = models.CharField(max_length=32)
    # 出生日期
    csrq = models.CharField(max_length=32)
    # 出生地
    csd = models.CharField(max_length=32)
    # 籍贯
    jg = models.CharField(max_length=32)
    # 政治面貌
    zzmm = models.CharField(max_length=32)
    # 民族
    mz = models.CharField(max_length=32)
    # 工号
    gh = models.CharField(max_length=32)
    # 工资号
    gzh = models.CharField(max_length=32)
    # 身份证号
    sfzh = models.CharField(max_length=32)
    # 职称（专业技术职务）
    zc = models.CharField(max_length=32)
    # 定制日期（评定日期）
    dzrq = models.CharField(max_length=32)
    # 学位（最高学位）
    xw = models.CharField(max_length=32)
    # 授予单位
    sydw = models.CharField(max_length=32)
    # 授予时间
    sysj = models.CharField(max_length=32)
    # 学历（最高学历，最后学历）
    xl = models.CharField(max_length=32)
    # 毕业院校
    byyx = models.CharField(max_length=32)
    # 毕业时间
    bysj = models.CharField(max_length=32)
    # 专业（所学专业）
    zy = models.CharField(max_length=32)
    # 从事专业
    cszy = models.CharField(max_length=32)
    # 所属学科
    ssxk = models.CharField(max_length=32)
    # 是否博导
    bd  = models.CharField(max_length=32)
    #是否硕导
    sd = models.CharField(max_length=32)
    # 研究方向
    yjfx = models.CharField(max_length=32)
    # 行政职务
    xzzw = models.CharField(max_length=32)
    # 主要社会兼职
    zyshjz = models.CharField(max_length=32)
    # 来校时间
    lxsj = models.CharField(max_length=32)
    # 外语语种
    wyyz = models.CharField(max_length=32)
    # 外语水平
    wysp = models.CharField(max_length=32)
    # 参加工作时间
    cjgzsj = models.CharField(max_length=32)
    # 工作单位
    gzdw = models.CharField(max_length=32)
    # 家庭住址
    jtzz = models.CharField(max_length=32)
    # 个人网站
    grwz = models.CharField(max_length=32)
    # 通讯地址
    txdz = models.CharField(max_length=32)
    # 邮政编码
    yzbm = models.CharField(max_length=32)
    # email格式
    email = models.CharField(max_length=32)
    # QQ号
    qq = models.CharField(max_length=32)
    # 联系电话
    lxdh = models.CharField(max_length=32)
    bgdh = models.CharField(max_length=32)
    # 办公电话
    yddh = models.CharField(max_length=32)
    # 秘书
    ms = models.CharField(max_length=32)
    # 秘书电话
    msdh = models.CharField(max_length=32)
    # 1寸照片
    yczp = models.ImageField(upload_to='')
    #2寸照片
    eczp = models.ImageField(upload_to='')
    #论文照片
    lwzp = models.ImageField(upload_to='')
    # 个人简历
    grjlCT = models.FileField(upload_to='')
    grjlC = models.FileField(upload_to='')
    grjlET = models.FileField(upload_to='')
    grjlE = models.FileField(upload_to='')
    # 备注
    bz = models.CharField(max_length=32)

class YSJB(models.Model):
    # 字段名称
    zdmc = models.CharField(max_length=32)
    # 含义
    hy = models.CharField(max_length=32)
    # 权限
    qx = models.CharField(max_length=32)
    # 同义词
    tyc = models.CharField(max_length=32)
    # 字段属性
    zdsx = models.CharField(max_length=32)
    # 取值范围
    qzfw = models.CharField(max_length=32)
    # 计算公式？？
    jsgs = models.CharField(max_length=32)
    # 备注
    bz = models.CharField(max_length=32)
class JYJL(models.Model):
    # 姓名
    xm = models.CharField(max_length=32)
    # 起止时间
    qzsj = models.CharField(max_length=32)
    # 学校
    xx = models.CharField(max_length=32)
    # 学历
    xl = models.CharField(max_length=32)
    # 学位
    xw = models.CharField(max_length=32)
    # 所学专业
    sxzy = models.CharField(max_length=32)
    # 导师
    ds = models.CharField(max_length=32)
    # 备注
    bz = models.CharField(max_length=32)
    class Meta:
        unique_together = ('xm', 'qzsj')
    primary  = ('xm','qzsj')
# 四、工作经历（文本或表格）GZJL
# 姓名，起止时间（主键：姓名 + 起止时间），工作单位，职务，承担任务，备注
class GZJL(models.Model):
    # 姓名
    xm = models.CharField(max_length=32)
    # 起止时间
    qzsj = models.CharField(max_length=32)
    # 工作单位
    gzdw = models.CharField(max_length=32)
    # 职务
    zw = models.CharField(max_length=32)
    # 承担任务
    cdrw = models.CharField(max_length=32)
    # 备注????
    bz = models.CharField(max_length=32)
    class Meta:
        unique_together = ('xm', 'qzsj')
    primary  = ('xm','qzsj')
# 五、职称经历ZCJL（主键：姓名+时间）
# 姓名，时间（年月，下同），教授
# 姓名，时间，副教授
# 姓名，时间，讲师
# 姓名，时间，助教
# 姓名，备注
class ZCJL(models.Model):
    # 姓名
    xm = models.CharField(max_length=32)
    # 时间格式与所要求不一致??????
    sj = models.CharField(max_length=32)
    # 职称
    zc = models.CharField(max_length=32)
    # 备注
    bz = models.CharField(max_length=32)
    class Meta:
        unique_together = ('xm', 'sj')
    primary = ('xm','sj')
# 六、党员相关DY
# 姓名（主键），入党时间，入党介绍人：（用逗号隔开），入党时所在支部，转正时间，现在支部，备注
class DY(models.Model):
    # 姓名
    xm = models.CharField(max_length=32, primary_key=True)
    # 入党时间
    rdsj = models.CharField(max_length=32)
    # 介绍人
    jsr = models.CharField(max_length=32)
    # 入党时所在支部
    szzb = models.CharField(max_length=32)
    # 转正时间???
    zzsj = models.CharField(max_length=32)
    # 现在支部
    xzzb = models.CharField(max_length=32)
    # 备注
    bz = models.CharField(max_length=32)
# 七、我的教学（分学期填写，每门课程一行，）
# 主键：姓名+起止时间+课程
# 起止时间=开始时间—结束时间
# 讲授课程（教学内容）
# 学生人数 （人数合计）
# 学生级别（研究生，本科生，高中生，初中生，小学生）
# 授课学时数（教学大纲上的理论学时，不是工作量）
# 工作量（学时）
#    工作量合计
# 备注
class WDJX(models.Model):
    # 姓名
    xm = models.CharField(max_length=32)
    # 起止时间
    qzsj = models.CharField(max_length=32)
    # 讲授课程(教学内容）
    jskc = models.CharField(max_length=32)
    # 学生人数（人数合计）
    xsrs = models.IntegerField()
    # 学生级别（研究生，本科生，高中生，初中生，小学生）
    xsjb = models.CharField(max_length=32)
    # 授课学时数（教学大纲洒净的理论学时，不是工作量）
    skxs = models.CharField(max_length=32)
    # 工作量（学时）
    gzl = models.CharField(max_length=32)
    # 工作量合计
    gzlhj = models.CharField(max_length=32)
    # 备注
    bz = models.CharField(max_length=32)
    class Meta:
        unique_together = ('xm', 'qzsj','jskc')
    primary  = ('xm','qzsj','jskc')
# 论文
class LW(models.Model):
    # 论文简称
    lwjc = models.CharField(max_length=32,primary_key=True)
    # 发表时间，包含年月即可？？？？
    fbsj = models.CharField(max_length=32)
    # 作者全称
    zzqc = models.CharField(max_length=32)
    # 作者简称
    zzjc = models.CharField(max_length=32)
    # 论文题目
    lwtm = models.CharField(max_length=32)
    # 发表刊物
    fbkw = models.CharField(max_length=32)
    # 论文其他信息【包括，收录情况（SCI,EI,SSCI,CSSCI，CPCI-S,CPCI-SSH），JCR分区（1,2,3,4），中科院分区（1,2,3,4），CCF分类，影响因子（IF），字数，ISSN号（CN号） DIO号等） 】，
    qtxx = models.CharField(max_length=32)
    # 是否通讯作者
    txzz = models.CharField(max_length=32)
    # 代表作排序（按重要性填写1, 2, 3
    # 等，不是代表作空着）
    dbz = models.CharField(max_length=32)
    # 依托项目（项目编号，用逗号隔开）
    ytxm = models.CharField(max_length=32)
    # 有关论文内容的字段用什么类型？？？
    lwqw = models.FileField(upload_to=None)
    lwsy = models.FileField(upload_to=None)
    lwytxmy = models.FileField(upload_to=None)
    lwfm = models.FileField(upload_to=None)
    lwml = models.FileField(upload_to=None)
    syzm = models.FileField(upload_to=None)
#横向项目
class HXXM(models.Model):
    # 项目简称
    xmjc = models.CharField(max_length=32)
    # 负责人
    fzr = models.CharField(max_length=32)
    # 项目名称
    xmmc = models.CharField(max_length=32)
    # 合同金额
    htje = models.CharField(max_length=32)
    # 签订日期
    qdrq = models.CharField(max_length=32)
    # 开始日期
    ksrq = models.CharField(max_length=32)
    # 计划完成日期
    jhwcrq = models.CharField(max_length=32)
    # 项目状态
    xmzt = models.CharField(max_length=32)
    # 项目组其他成员（用逗号隔开）
    qtcy = models.CharField(max_length=32)
    # 本人位次
    brwc = models.CharField(max_length=32)
    # 对方单位名称
    dwmc = models.CharField(max_length=32)
    # 对方地址
    dz = models.CharField(max_length=32)
    # 对方联系人姓名
    lxrxm = models.CharField(max_length=32)
    # 联系电话
    lxdh = models.CharField(max_length=32)
    # 项目合同书
    xmhts = models.FileField()
    # 项目附加合同书
    xmfjhts = models.FileField()
    # 结题报告
    jtbg = models.FileField()
    # 项目其他文档
    xmqtwd = models.FileField()
    #备注
    bz = models.CharField(max_length=32)
# 纵向项目
class ZXXM(models.Model):
    # 项目简称
    xmjc = models.CharField(max_length=32,primary_key=True)
    # 负责人
    fzr = models.CharField(max_length=32)
    # 项目名称
    xmmc = models.CharField(max_length=32)
    # 项目级别
    xmjb = models.CharField(max_length=32)
    # 项目编号
    xmbh = models.CharField(max_length=32)
    # 项目来源单位
    xmlydw = models.CharField(max_length=32)
    # 项目类别
    xmlb = models.CharField(max_length=32)
    # 项目经费
    xmjf = models.CharField(max_length=32)
    # 立项日期
    lxrq = models.CharField(max_length=32)
    # 开始日期
    kssj = models.CharField(max_length=32)
    # 计划完成日期
    jhwcrq = models.CharField(max_length=32)
    # 项目组其他成员(用逗号隔开)
    xmzqtcy = models.CharField(max_length=32)
    # 项目申请书
    xmsqs = models.FileField(upload_to=None)
    #立项批准书
    lxpzs = models.FileField(upload_to=None)
    # 其他文档
    qtwd = models.FileField(upload_to=None)
    # 备注
    bz = models.CharField(max_length=32)
# 获奖情况
class HJQK(models.Model):
    # 奖励简称
    jxjc = models.CharField(max_length=32)
    # 奖励类别
    jllb = models.CharField(max_length=32)
    # 成果名称
    cgmc = models.CharField(max_length=32)
    # 获奖人
    hjr = models.CharField(max_length=32)
    # 获奖人数
    hjrs = models.CharField(max_length=32)
    # 发证机关
    fzjg = models.CharField(max_length=32)
    # 获奖日期
    hjrq = models.CharField(max_length=32)
    # 获奖级别
    hjjb = models.CharField(max_length=32)
    # 获奖等级
    hjdj = models.CharField(max_length=32)
    # 获奖人员名单
    hjrymd = models.CharField(max_length=32)
    # 本人位次
    brwc = models.CharField(max_length=32)
    # 获奖证书
    hjzs = models.FileField(upload_to=None)
    # 备注
    bz = models.CharField(max_length=32)

# 专利
class ZL(models.Model):
    # 专利简称
    zljc = models.CharField(max_length=32)
    # 第一位发明人
    dywfmr = models.CharField(max_length=32)
    # 发明名称
    fmmc = models.CharField(max_length=32)
    # 专利类型
    zllx = models.CharField(max_length=32)
    # 专利范围（国内，国外）
    zlfw = models.CharField(max_length=32)
    # 专利状态（授理，授权）
    zlzt = models.CharField(max_length=32)
    # 申请号
    sqh = models.CharField(max_length=32)
    # 专利申请日
    zlsqr = models.CharField(max_length=32)
    # 授权公告日
    sqggr = models.CharField(max_length=32)
    # 授权公告号
    sqggh = models.CharField(max_length=32)
    # 其他发明人
    qtfmr = models.CharField(max_length=32)
    # 备注
    bz = models.CharField(max_length=32)
    # 专利受理通知书文件名（专利简称（含年份）+受理））
    zlsltzswjm = models.CharField(max_length=32)
    # 专利证书
    zlzs = models.FileField(upload_to=None)
    # 其他文档
    qtwd = models.FileField(upload_to=None)
#荣誉称号
class RYCH(models.Model):
    # 获得者
    hdz = models.CharField(max_length=32)
    # 获得时间
    hdsj = models.CharField(max_length=32)
    # 称号名称
    chmc = models.CharField(max_length=32)
    # 级别
    jb = models.CharField(max_length=32)
    # 批准机关
    pzjg = models.CharField(max_length=32)
    #本人位次
    brwc = models.CharField(max_length=32)
    # 备注
    bz = models.CharField(max_length=32)
    # 荣誉证书
    ryzs = models.FileField(upload_to=None)
# 软件著作权
class RJZZQ(models.Model):
    # 著作权简称
    zzqjc = models.CharField(max_length=32,primary_key=True)
    # 申请人
    sqr = models.CharField(max_length=32)
    # 著作权名称
    zzqmc = models.CharField(max_length=32)
    # 著作权编号
    zzqbh = models.CharField(max_length=32)
    # 登记号
    djh = models.CharField(max_length=32)
    # 获得时间
    hdsj = models.CharField(max_length=32)
    # 著作权人
    zzqr = models.CharField(max_length=32)
    # 备注
    bz = models.CharField(max_length=32)
    # 著作权证书
    zzqzs = models.FileField(upload_to=None)
# 著作
class ZZ(models.Model):
    # 著作简称
    zzjc = models.CharField(max_length=32)
    # 著作名称
    zzmc = models.CharField(max_length=32)
    # 出版时间
    cbsj = models.CharField(max_length=32)
    # 出版地
    cbd = models.CharField(max_length=32)
    # 著作类别
    zzlb  = models.CharField(max_length=32)
    # 总字数（万字）
    zzs = models.CharField(max_length=32)
    #语种
    yz = models.CharField(max_length=32)
    # 出版单位
    cbdw = models.CharField(max_length=32)
    # 作者信息
    zzxx = models.CharField(max_length=32)
    # 备注
    bz = models.CharField(max_length=32)
    # 电子文档
    dzwd = models.FileField(upload_to=None)
# 其他成果
class QTCG(models.Model):
    # 成果简称
    cgjc = models.CharField(max_length=32)
    # 成果类别
    cglb = models.CharField(max_length=32)
    # 成果名称
    cgmc = models.CharField(max_length=32)
    # 获得时间
    hdsj = models.CharField(max_length=32)
    # 颁发部门
    bfbm = models.CharField(max_length=32)
    # 成果编号
    cgbh = models.CharField(max_length=32)
    # 作者信息
    zzxx = models.CharField(max_length=32)
    # 备注
    bz = models.CharField(max_length=32)
    # 电子文档
    dzwd = models.FileField(upload_to=None)
# 我的学生
class WDXS(models.Model):
    # 中文姓名
    zwxm = models.CharField(max_length=32,primary_key=True)
    # 英文全名
    ywqm = models.CharField(max_length=32)
    # 英文简名
    ywjm = models.CharField(max_length=32)
    # 性别
    xb = models.CharField(max_length=32)
    # 学号
    xh = models.CharField(max_length=32)
    # 出生日期
    csrq = models.CharField(max_length=32)
    # 学习方式
    xxfs = models.CharField(max_length=32)
    # 入学日期，格式为年月
    rxrq = models.CharField(max_length=32)
    # 毕业论文题目
    bylwtm = models.CharField(max_length=32)
    # 学位类别
    xwlb = models.CharField(max_length=32)
    # 研究方向
    yjfx = models.CharField(max_length=32)
    # 导师
    ds = models.CharField(max_length=32)
    # 副导师
    fds = models.CharField(max_length=32)
    # 学生类型
    xslx = models.CharField(max_length=32)
    # 联系电话
    lxdh = models.CharField(max_length=32)
    # email
    email = models.CharField(max_length=32)
    # 身份证号
    sfzh = models.CharField(max_length=32)
    # 毕业日期，格式为年月
    byrq = models.CharField(max_length=32)
    # 毕业去向
    byqx = models.CharField(max_length=32)
    # 备注
    bz = models.CharField(max_length=32)
