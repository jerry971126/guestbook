from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Message

#留言列表
class MessageList(ListView):
    model = Message
    ordering = ["-id"]      #以id欄位值由大至小反向順序
# 留言檢視
class MessageDetail(DetailView):
    model = Message

# 新增留言
class MessageCreate(CreateView):
    model = Message
    fields = ['user', 'subject', 'content']     # 僅顯示 user, subject, content 這 3 個欄位
    success_url = reverse_lazy('msg_list')                   # 新增成功後，導向留言列表
# Create your views here.
# 刪除留言
class MessageDelete(DeleteView):
    model = Message
    success_url = reverse_lazy('msg_list')               # 刪除成功返回留言列表
