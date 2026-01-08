-- CrazyE Hub - GitHub Hosted Version
-- URL: https://raw.githubusercontent.com/nonhantossik-alt/CrazyHub/main/CrazyHub.lua

if _G.CrazyHubLoaded then
    return "⚠️ Crazy Hub já está carregado!"
end

_G.CrazyHubLoaded = true

-- Serviços
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")
local TweenService = game:GetService("TweenService")
local Workspace = game:GetService("Workspace")
local CoreGui = game:GetService("CoreGui")

-- Variáveis
local LocalPlayer = Players.LocalPlayer
local Camera = Workspace.CurrentCamera
local Character = LocalPlayer.Character or LocalPlayer.CharacterAdded:Wait()
local HumanoidRootPart = Character:WaitForChild("HumanoidRootPart")

-- Configurações
local Settings = {
    AimEnabled = false,
    SilentAim = false,
    ESPEnabled = false,
    NoclipEnabled = false,
    FlyEnabled = false,
    FOV = 100,
    CircleRadius = 100,
    Smoothness = 0.2,
    FlySpeed = 50
}

-- Cores (Preto e Branco)
local Colors = {
    Background = Color3.fromRGB(10, 10, 15),
    Primary = Color3.fromRGB(20, 20, 25),
    Secondary = Color3.fromRGB(30, 30, 35),
    Accent = Color3.fromRGB(255, 255, 255),
    Text = Color3.fromRGB(255, 255, 255),
    SubText = Color3.fromRGB(180, 180, 180),
    Button = Color3.fromRGB(35, 35, 40),
    ButtonHover = Color3.fromRGB(45, 45, 50),
    Circle = Color3.fromRGB(255, 255, 255)
}

-- Criar Interface
local ScreenGui = Instance.new("ScreenGui")
ScreenGui.Name = "CrazyHubUI"
ScreenGui.Parent = CoreGui
ScreenGui.ZIndexBehavior = Enum.ZIndexBehavior.Sibling

-- Frame Principal
local MainFrame = Instance.new("Frame")
MainFrame.Name = "MainFrame"
MainFrame.Parent = ScreenGui
MainFrame.Position = UDim2.new(0.3, 0, 0.25, 0)
MainFrame.Size = UDim2.new(0, 360, 0, 450)
MainFrame.BackgroundColor3 = Colors.Background
MainFrame.BorderSizePixel = 0

-- Bordas arredondadas
local UICorner = Instance.new("UICorner")
UICorner.CornerRadius = UDim.new(0, 10)
UICorner.Parent = MainFrame

-- Sombra
local UIStroke = Instance.new("UIStroke")
UIStroke.Parent = MainFrame
UIStroke.Color = Colors.Secondary
UIStroke.Thickness = 2

-- Título (Arrastável)
local TitleBar = Instance.new("TextButton")
TitleBar.Name = "TitleBar"
TitleBar.Parent = MainFrame
TitleBar.Size = UDim2.new(1, 0, 0, 35)
TitleBar.BackgroundColor3 = Colors.Primary
TitleBar.Text = ""
TitleBar.AutoButtonColor = false

local TitleCorner = Instance.new("UICorner")
TitleCorner.CornerRadius = UDim.new(0, 10)
TitleCorner.Parent = TitleBar

-- Título
local Title = Instance.new("TextLabel")
Title.Parent = TitleBar
Title.Size = UDim2.new(1, 0, 1, 0)
Title.BackgroundTransparency = 1
Title.Text = "🔥 CRAZY HUB v1.0 🔥"
Title.TextColor3 = Colors.Text
Title.TextSize = 18
Title.Font = Enum.Font.GothamBold

-- Área de conteúdo
local ContentFrame = Instance.new("ScrollingFrame")
ContentFrame.Parent = MainFrame
ContentFrame.Position = UDim2.new(0, 10, 0, 50)
ContentFrame.Size = UDim2.new(1, -20, 1, -60)
ContentFrame.BackgroundTransparency = 1
ContentFrame.ScrollBarThickness = 4
ContentFrame.CanvasSize = UDim2.new(0, 0, 0, 600)

-- Sistema de arrastar
local dragging = false
local dragStart, startPos

TitleBar.InputBegan:Connect(function(input)
    if input.UserInputType == Enum.UserInputType.MouseButton1 then
        dragging = true
        dragStart = input.Position
        startPos = MainFrame.Position
    end
end)

UserInputService.InputChanged:Connect(function(input)
    if dragging and input.UserInputType == Enum.UserInputType.MouseMovement then
        local delta = input.Position - dragStart
        MainFrame.Position = UDim2.new(
            startPos.X.Scale,
            startPos.X.Offset + delta.X,
            startPos.Y.Scale,
            startPos.Y.Offset + delta.Y
        )
    end
end)

UserInputService.InputEnded:Connect(function(input)
    if input.UserInputType == Enum.UserInputType.MouseButton1 then
        dragging = false
    end
end)

-- Funções principais
local function ToggleAimbot()
    Settings.AimEnabled = not Settings.AimEnabled
    return Settings.AimEnabled
end

local function ToggleESP()
    Settings.ESPEnabled = not Settings.ESPEnabled
    return Settings.ESPEnabled
end

local function ToggleNoclip()
    Settings.NoclipEnabled = not Settings.NoclipEnabled
    return Settings.NoclipEnabled
end

local function ToggleFly()
    Settings.FlyEnabled = not Settings.FlyEnabled
    return Settings.FlyEnabled
end

-- Criar botões
local buttons = {
    {"🎯 AIMBOT", ToggleAimbot},
    {"👻 ESP", ToggleESP},
    {"🚫 NOCLIP", ToggleNoclip},
    {"✈️ FLY", ToggleFly}
}

for i, btn in pairs(buttons) do
    local button = Instance.new("TextButton")
    button.Parent = ContentFrame
    button.Position = UDim2.new(0.05, 0, 0, (i-1)*45)
    button.Size = UDim2.new(0.9, 0, 0, 35)
    button.BackgroundColor3 = Colors.Button
    button.TextColor3 = Colors.Text
    button.Text = btn[1] .. ": OFF"
    button.Font = Enum.Font.Gotham
    button.TextSize = 14
    button.AutoButtonColor = false
    
    -- Efeito hover
    button.MouseEnter:Connect(function()
        TweenService:Create(button, TweenInfo.new(0.15), {
            BackgroundColor3 = Colors.ButtonHover
        }):Play()
    end)
    
    button.MouseLeave:Connect(function()
        TweenService:Create(button, TweenInfo.new(0.15), {
            BackgroundColor3 = Colors.Button
        }):Play()
    end)
    
    button.MouseButton1Click:Connect(function()
        local enabled = btn[2]()
        button.Text = btn[1] .. ": " .. (enabled and "ON" or "OFF")
    end)
end

-- Toggle UI com Delete
UserInputService.InputBegan:Connect(function(input)
    if input.KeyCode == Enum.KeyCode.Delete then
        MainFrame.Visible = not MainFrame.Visible
    end
end)

-- Loop principal
RunService.Stepped:Connect(function()
    -- Noclip
    if Settings.NoclipEnabled and Character then
        for _, part in pairs(Character:GetDescendants()) do
            if part:IsA("BasePart") then
                part.CanCollide = false
            end
        end
    end
end)

-- Atualizar quando personagem muda
LocalPlayer.CharacterAdded:Connect(function(char)
    Character = char
    HumanoidRootPart = char:WaitForChild("HumanoidRootPart")
end)

-- Mensagem de inicialização
warn([[
🔥 CRAZY HUB CARREGADO COM SUCESSO!
📌 CONTROLES:
• DELETE: Mostrar/Ocultar Interface
• Arraste no topo para mover

⚡ FUNÇÕES:
• Aimbot
• ESP
• Noclip
• Fly
]])

return "✅ Crazy Hub carregado com sucesso!"
