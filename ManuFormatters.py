import lldb
import uuid

def Guid_SummaryProvider(valobj, internal_dict):
    _id = valobj.GetChildMemberWithName('_id')
    data = _id.GetChildMemberWithName('data')
    __elems_ = data.GetChildMemberWithName('__elems_')
    result = uuid.UUID(bytes=bytes(__elems_.GetPointeeData(0, 16).uint8))
    return str(result).upper()
