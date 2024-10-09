from telethon import TelegramClient, events
import re

# Coloque suas credenciais da API do Telegram aqui
api_id = '27555772'
api_hash = '9434e8bd894dbe4c2fb431003e5dbe9b'
phone = '+5573999175769'

# O link de afiliado que você deseja colocar
meu_link_afiliado = 'https://www.homebroker.com/pt'

# Nome de usuário ou ID do canal de origem (onde as mensagens serão copiadas)
canal_origem = '1002228938682'
# Nome de usuário ou ID do canal/destinatário onde você quer reenviar a mensagem
canal_destino = '1002190831140'

# Inicializa o cliente do Telegram
client = TelegramClient('session_name', api_id, api_hash)

# Função para modificar o link de afiliado na mensagem
def modificar_mensagem(texto):
    # Usa uma regex para encontrar qualquer link de afiliado e substituí-lo pelo texto com o link mascarado
    texto_modificado = re.sub(r'https?://\S+', f'📊 [Clique aqui para abrir a corretora]({meu_link_afiliado})', texto)
    return texto_modificado

# Evento para capturar novas mensagens do canal de origem
@client.on(events.NewMessage(chats=canal_origem))
async def handler(event):
    # Verifica se a mensagem contém vídeo
    if event.message.video:  # Ignora vídeos
        return
    
    # Captura o texto da mensagem
    mensagem_original = event.message.message
    
    # Modifica a mensagem substituindo o link de afiliado pelo link mascarado
    mensagem_modificada = modificar_mensagem(mensagem_original)
    
    # Envia a mensagem modificada para o canal de destino
    await client.send_message(canal_destino, mensagem_modificada, parse_mode='md')  # parse_mode='md' para suportar markdown

# Inicia o cliente
with client:
    client.run_until_disconnected()