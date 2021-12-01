attrs = []
for i in range(0, 300):
    user_attribute = looker_sdk.models.WriteUserAttribute()
    user_attribute.type = "string"
    user_attribute.default_value = ""
    user_attribute.value_is_hidden = False
    user_attribute.user_can_view = True
    user_attribute.user_can_edit = False
    user_attribute.name = f"customVarLabel{i}"
    user_attribute.label = f"custom Var Label {i}"
    attrs.append(user_attribute)

for attr in attrs:
    sdk.create_user_attribute(attr)
