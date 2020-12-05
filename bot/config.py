class config:
    BOT_TOKEN = "1477482400:AAFDFcZX1bDvWMLPxu_3uR5dJ5upTyxvTVI"
    APP_ID = "2163116"
    API_HASH = "5216596d95424259ba895069540d39cb"
    DATABASE_URL = "postgres://bgrqodynwqnida:02f56ebce7291ea718fade67ff6f481f1bd19084ddc7a08ccc064908efb8c451@ec2-54-237-135-248.compute-1.amazonaws.com:5432/dvn5q7ulm0mur"
    SUDO_USERS = "1202000664 1043474763" # Sepearted by space.
    SUPPORT_CHAT_LINK = "https://t.me/joinchat/R6UTGBPMnj0pJ6l90ibnSg"
    DOWNLOAD_DIRECTORY = "./downloads/"


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  Ytdl = ['ytdl']

class Messages:
    START_MSG = "**Hi there {}.**\n__I'm Google Drive Uploader Bot.You can use me to upload any file / video to Google Drive from direct link or Telegram Files.__\n__You can know more from /help.__"

    HELP_MSG = [
        ".",
        "**Google Drive Uploader**\n__Você pode fazer upload de arquivos através do link direto ou arquivos do telegram para o seu Google Drive. Só é necessário me autenticar em sua conta do Google Drive e enviar um link de download direto ou arquivo de telegram.__\n\nTenho mais recursos ...! Quer saber mais sobre isso? Basta percorrer este tutorial e ler as mensagens com atenção.",
        
        f"**Autenticação com Google Drive**\n__Envie o comando /{BotCommands.Authorize[0]} e você receberá uma URL, visite a URL e siga os passos e envie o código recebido aqui. Usar /{BotCommands.Revoke[0]} para revogar sua conta do Google Drive atualmente registrada.__\n\n**Nota: Eu não vou ouvir nenhum comando ou mensagem (exceto /{BotCommands.Authorize[0]} commmand) até você me autorizar.\nPortanto, a autorização é obrigatória !**",
        
        f"**Direct Links**\n__Envie-me um link de download direto de um arquivo e farei o download em meu servidor e carregarei para sua conta do Google Drive. Você pode renomear arquivos antes de carregá-los na conta GDrive. Basta me enviar o URL e o novo nome de arquivo separados por ' | '.__\n\n**__Exemplos:__**\n```https://example.com/AFileWithDirectDownloadLink.mkv | New FileName.mkv```\n\n**Telegram Files**\n__Para fazer upload de arquivos do telegram em sua conta do Google Drive, basta me enviar o arquivo e eu irei fazer o download e enviar para sua conta do Google Drive. Nota: O download dos arquivos do Telegram é lento. pode demorar mais para arquivos grandes.__\n\n**YouTube-DL Support**\n__Download de pastas via youtube-dl.\nUse /{BotCommands.Ytdl[0]} (YouTube Link/YouTube-DL Supported site link)__",
        
        f"**Pasta personalizada para upload**\n__Deseja fazer upload em uma pasta personalizada ou no__ ** TeamDrive** __ ?\nUse /{BotCommands.SetFolder[0]} (URL DA PASTA) para definir a pasta de upload personalizada.\nTodos os arquivos são carregados na pasta personalizada que você fornece.__",
        
        f"**Apagar Pastas Google Drive**\n__Exclua os arquivos do Google Drive. Usar /{BotCommands.Delete[0]} (File/Folder URL) para excluir o arquivo.\nVocê também pode esvaziar arquivos de lixo usando /{BotCommands.EmptyTrash[0]}\nNota: os arquivos são excluídos permanentemente. Este processo não pode ser desfeito.\n\n**Copiar Pastas do Google Drive**\n__Sim, clone ou copie arquivos do Google Drive.\n__Use /{BotCommands.Clone[0]} (File id / Folder id or URL) para copiar arquivos do Google Drive em sua conta do Google Drive.__",
        
        "**Regras e Precauções**\n__1. Não copie arquivos / pastas do Google Drive GRANDES. Ele pode travar o bot e seus arquivos podem ser danificados.\n2. Envie uma solicitação por vez, a menos que o bot interrompa todos os processos.\n3. Não envie links lentos @transload primeiro.\n4. Não abuse, sobrecarregue ou abuse deste serviço gratuito.__",
        
        # Dont remove this ↓ if you respect developer.
        "**Developed by @viperadnan**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **Limite de taxa excedido.**\n__Limite de taxa de usuário excedido, tente após 24 horas.__"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **Arquivo/Pasta não encontrado.**\n__File id - {} Não encontrado. Certifique-se\'s existe e acessível pela conta registrada.__"
    
    INVALID_GDRIVE_URL = "❗ **URL inválida do Google Drive**\nCertifique-se de que o URL do Google Drive esteja em um formato válido."
    
    COPIED_SUCCESSFULLY = "✅ **Copiado com sucesso.**\n[{}]({}) __({})__"
    
    NOT_AUTH = f"🔑 **Você não me autenticou para enviar para qualquer conta.**\n__Send /{BotCommands.Authorize[0]} para autenticar.__"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Carregando arquivo...**\n**Filename:** ```{}```\n**Size:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **Carregado com sucesso.**\n[{}]({}) __({})__"
    
    DOWNLOAD_ERROR = "❗**O downloader falhou**\n{}\n__Link - {}__"
    
    DOWNLOADING = "📥 **Baixando arquivo...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **Já autorizou sua conta do Google Drive.**\n__Use /revoke para revogar a conta corrente.__\n__Envie-me um link direto ou arquivo para fazer upload no Google Drive__"
    
    FLOW_IS_NONE = f"❗ **Código inválido**\n__Run {BotCommands.Authorize[0]} first.__"
    
    AUTH_SUCCESSFULLY = '🔐 **Conta autorizada do Google Drive com sucesso.**'
    
    INVALID_AUTH_CODE = '❗ **Código inválido**\n__O código que você enviou é inválido ou já foi usado antes. Gere um novo pelo URL de autorização__'
    
    AUTH_TEXT = "⛓️ **Para autorizar sua conta do Google Drive, visite este [URL]({}) e envie o código gerado aqui.**\n__Visite o URL > Permitir permissões > você receberá um código > copie > copie agora__"
    
    DOWNLOAD_TG_FILE = "📥 **Downloading File...**\n**Filename:** ```{}```\n**Size:** ```{}```\n**MimeType:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **Link de pasta personalizada definido com sucesso.**\n__Your custom folder id - {}\nUse__ ```/{} clear``` __to clear it.__'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **ID de pasta personalizada apagada com sucesso.**\n__Use__ ```/{BotCommands.SetFolder[0]} (Folder Link)``` __para colocá-lo de volta__.'
    
    CURRENT_PARENT = "🆔 **Seu ID de pasta personalizada atual - {}**\n__Use__ ```/{} (Folder link)``` __mudar isso.__"
    
    REVOKED = f"🔓 **Conta atual registrada revogada com sucesso.**\n__Use /{BotCommands.Authorize[0]} para autenticar novamente e usar este bot.__"
    
    NOT_FOLDER_LINK = "❗ **Link de pasta inválido.**\n__O link que você enviou não pertence a uma pasta.__"
    
    CLONING = "🗂️ **Clonagem no Google Drive...**\n__G-Drive Link - {}__"
    
    PROVIDE_GDRIVE_URL = "**❗ Forneça um URL válido do Google Drive junto com o comando.**\n__Usage - /{} (GDrive Link)__"
    
    INSUFFICIENT_PERMISSONS = "❗ **Você não tem permissões suficientes para este arquivo.**\n__File id - {}__"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **Arquivo excluído com sucesso.**\n__Arquivo excluído permanentemente !\nFile id - {}__"
    
    WENT_WRONG = "⁉️ **ERRO: ALGO FOI ERRADO**\n__Por favor, tente novamente mais tarde.__"
    
    EMPTY_TRASH = "🗑️🚮**Lixeira esvaziada com sucesso !**"
    
    PROVIDE_YTDL_LINK = "❗**Forneça um link válido do YouTube-DL compatível.**"
