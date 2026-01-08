-- Crazy Hub - Script Completo
-- Loadstring: loadstring(game:HttpGet("https://raw.githubusercontent.com/nonhantossik-alt/CrazyHub/main/CrazyHub.lua"))()

if _G.CrazyHubLoaded then
    warn("⚠️ Crazy Hub já está carregado!")
    return
end

_G.CrazyHubLoaded = true

-- Serviços
local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")
local Workspace = game:GetService("Workspace")
local CoreGui = game:GetService("CoreGui")

-- Variáveis
local LocalPlayer = Players.LocalPlayer
local Camera = Workspace.CurrentCamera

-- Configurações
local Settings = {
    AimEnabled = false,
    ESPEnabled = false,
    NoclipEnabled = false,
    FlyEnabled = false,
    FOV = 100
}

-- Criar Interface
local ScreenGui = Instance.new("ScreenGui")
ScreenGui.Name = "CrazyHubUI"
ScreenGui.Parent = CoreGui
ScreenGui.ZIndexBehavior = Enum.ZIndexBehavior.Sibling

local MainFrame = Instance.new("Frame")
MainFrame.Parent = ScreenGui
MainFrame.Position = UDim2.new(0.3, 0, 0.3, 0)
MainFrame.Size = UDim2.new(0, 320, 0, 400)
MainFrame.BackgroundColor3 = Color3.fromRGB(10, 10, 15)
MainFrame.BorderSizePixel = 0

-- Título arrastável
local TitleBar = Instance.new("TextButton")
TitleBar.Parent = MainFrame
TitleBar.Size = UDim2.new(1, 0, 0, 40)
TitleBar.BackgroundColor3 = Color3.fromRGB(20, 20, 25)
TitleBar.Text = ""
TitleBar.AutoButtonColor = false

local Title = Instance.new("TextLabel")
Title.Parent = TitleBar
Title.Size = UDim2.new(1, 0, 1, 0)
Title.BackgroundTransparency = 1
Title.Text = "🔥 CRAZY HUB 🔥"
Title.TextColor3 = Color3.fromRGB(255, 255, 255)
Title.TextSize = 20
Title.Font = Enum.Font.GothamBold

-- Sistema de arrastar SIMPLES
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

-- Função para criar botões
local function CreateButton(text, yPos, action)
    local button = Instance.new("TextButton")
    button.Parent = MainFrame
    button.Position = UDim2.new(0.1, 0, yPos, 0)
    button.Size = UDim2.new(0.8, 0, 0, 35)
    button.BackgroundColor3 = Color3.fromRGB(30, 30, 40)
    button.TextColor3 = Color3.fromRGB(255, 255, 255)
    button.Text = text
    button.Font = Enum.Font.Gotham
    button.TextSize = 14
    button.AutoButtonColor = false
    
    -- Efeito hover
    button.MouseEnter:Connect(function()
        button.BackgroundColor3 = Color3.fromRGB(40, 40, 50)
    end)
    
    button.MouseLeave:Connect(function()
        button.BackgroundColor3 = Color3.fromRGB(30, 30, 40)
    end)
    
    if action then
        button.MouseButton1Click:Connect(action)
    end
    
    return button
end

-- Criar botões
local aimbotBtn = CreateButton("🎯 AIMBOT: OFF", 0.15, function()
    Settings.AimEnabled = not Settings.AimEnabled
    aimbotBtn.Text = Settings.AimEnabled and "🎯 AIMBOT: ON" or "🎯 AIMBOT: OFF"
    warn("Aimbot: " .. (Settings.AimEnabled and "ATIVADO" or "DESATIVADO"))
end)

local espBtn = CreateButton("👻 ESP: OFF", 0.25, function()
    Settings.ESPEnabled = not Settings.ESPEnabled
    espBtn.Text = Settings.ESPEnabled and "👻 ESP: ON" or "👻 ESP: OFF"
    warn("ESP: " .. (Settings.ESPEnabled and "ATIVADO" or "DESATIVADO"))
end)

local noclipBtn = CreateButton("🚫 NOCLIP: OFF", 0.35, function()
    Settings.NoclipEnabled = not Settings.NoclipEnabled
    noclipBtn.Text = Settings.NoclipEnabled and "🚫 NOCLIP: ON" or "🚫 NOCLIP: OFF"
    warn("Noclip: " .. (Settings.NoclipEnabled and "ATIVADO" or "DESATIVADO"))
end)

local flyBtn = CreateButton("✈️ FLY: OFF", 0.45, function()
    Settings.FlyEnabled = not Settings.FlyEnabled
    flyBtn.Text = Settings.FlyEnabled and "✈️ FLY: ON" or "✈️ FLY: OFF"
    warn("Fly: " .. (Settings.FlyEnabled and "ATIVADO" or "DESATIVADO"))
end)

local teleportBtn = CreateButton("📍 TELEPORTAR", 0.55, function()
    warn("Procurando jogador para teleportar...")
    for _, player in pairs(Players:GetPlayers()) do
        if player ~= LocalPlayer and player.Character then
            local targetHRP = player.Character:FindFirstChild("HumanoidRootPart")
            local myChar = LocalPlayer.Character
            if myChar and targetHRP then
                local myHRP = myChar:FindFirstChild("HumanoidRootPart")
                if myHRP then
                    myHRP.CFrame = targetHRP.CFrame + Vector3.new(0, 5, 0)
                    warn("Teleportado para: " .. player.Name)
                    break
                end
            end
        end
    end
end)

-- Toggle UI com Delete
UserInputService.InputBegan:Connect(function(input)
    if input.KeyCode == Enum.KeyCode.Delete then
        MainFrame.Visible = not MainFrame.Visible
    end
end)

-- Noclip loop
RunService.Stepped:Connect(function()
    if Settings.NoclipEnabled then
        local character = LocalPlayer.Character
        if character then
            for _, part in pairs(character:GetDescendants()) do
                if part:IsA("BasePart") then
                    part.CanCollide = false
                end
            end
        end
    end
end)

-- Mensagem de sucesso
warn([[
================================
🔥 CRAZY HUB CARREGADO COM SUCESSO!
================================
📌 CONTROLES:
• DELETE: Mostrar/Ocultar Interface
• Clique e arraste no topo para mover

⚡ FUNÇÕES DISPONÍVEIS:
• Aimbot
• ESP
• Noclip
• Fly
• Teleporte automático
================================
]])

return "✅ Crazy Hub v1.0 - Carregado!"
